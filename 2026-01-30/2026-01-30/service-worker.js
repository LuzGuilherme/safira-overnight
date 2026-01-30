// Service Worker for Triathlon Dashboard PWA
const CACHE_NAME = 'triathlon-dashboard-v2.1';
const STATIC_ASSETS = [
  './',
  './triathlon-dashboard.html',
  './manifest.json',
  'https://cdn.jsdelivr.net/npm/chart.js'
];

// Install event - cache static assets
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      console.log('Caching static assets');
      return cache.addAll(STATIC_ASSETS);
    })
  );
  self.skipWaiting();
});

// Activate event - clean old caches
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys.filter(key => key !== CACHE_NAME)
            .map(key => caches.delete(key))
      );
    })
  );
  self.clients.claim();
});

// Fetch event - network first, fallback to cache
self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);
  
  // Skip non-GET requests
  if (event.request.method !== 'GET') return;
  
  // Skip Supabase API requests (always fetch fresh)
  if (url.hostname.includes('supabase.co')) {
    return;
  }
  
  event.respondWith(
    fetch(event.request)
      .then(response => {
        // Clone response and cache it
        const responseClone = response.clone();
        caches.open(CACHE_NAME).then(cache => {
          cache.put(event.request, responseClone);
        });
        return response;
      })
      .catch(() => {
        // Fallback to cache
        return caches.match(event.request);
      })
  );
});

// Background sync for offline support
self.addEventListener('sync', event => {
  if (event.tag === 'sync-data') {
    console.log('Background sync triggered');
  }
});
