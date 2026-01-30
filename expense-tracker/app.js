/**
 * Expense Tracker Dashboard
 * Loads data from data.json and renders charts + tables
 */

// Global state
let dashboardData = null;
let trendsChart = null;
let categoriesChart = null;
let currentPage = 1;
const itemsPerPage = 20;
let filteredTransactions = [];

// Chart.js global config
Chart.defaults.color = '#a0a0b0';
Chart.defaults.borderColor = '#2a2a38';
Chart.defaults.font.family = "'Inter', sans-serif";

// Category colors
const categoryColors = {
    alimentacao: { bg: '#ef4444', border: '#dc2626' },
    transportes: { bg: '#f59e0b', border: '#d97706' },
    casa: { bg: '#3b82f6', border: '#2563eb' },
    saude: { bg: '#10b981', border: '#059669' },
    lazer: { bg: '#8b5cf6', border: '#7c3aed' },
    vestuario: { bg: '#ec4899', border: '#db2777' },
    tecnologia: { bg: '#06b6d4', border: '#0891b2' },
    trabalho: { bg: '#6366f1', border: '#4f46e5' },
    fitness: { bg: '#f97316', border: '#ea580c' },
    educacao: { bg: '#14b8a6', border: '#0d9488' },
    outros: { bg: '#6b7280', border: '#4b5563' },
    transferencias: { bg: '#a855f7', border: '#9333ea' },
    salario: { bg: '#22c55e', border: '#16a34a' }
};

// Initialize dashboard
document.addEventListener('DOMContentLoaded', async () => {
    await loadData();
});

async function loadData() {
    const loading = document.getElementById('loading');
    const emptyState = document.getElementById('empty-state');
    
    try {
        const response = await fetch('data.json');
        
        if (!response.ok) {
            throw new Error('Data file not found');
        }
        
        dashboardData = await response.json();
        
        if (!dashboardData.stats || dashboardData.stats.total_transactions === 0) {
            loading.classList.add('hidden');
            emptyState.style.display = 'flex';
            return;
        }
        
        renderDashboard();
        loading.classList.add('hidden');
        
    } catch (error) {
        console.error('Error loading data:', error);
        loading.classList.add('hidden');
        emptyState.style.display = 'flex';
    }
}

function refreshData() {
    location.reload();
}

function renderDashboard() {
    renderStats();
    renderTrendsChart();
    renderCategoriesChart();
    renderCategoriesGrid();
    populateCategoryFilter();
    filterTransactions();
    updateLastUpdate();
}

function renderStats() {
    const { stats } = dashboardData;
    
    document.getElementById('total-income').textContent = formatCurrency(stats.total_income);
    document.getElementById('total-expenses').textContent = formatCurrency(stats.total_expenses);
    document.getElementById('net-balance').textContent = formatCurrency(stats.net_balance);
    document.getElementById('total-transactions').textContent = stats.total_transactions.toLocaleString('pt-PT');
    
    // Update period badge
    if (stats.first_date && stats.last_date) {
        const first = formatDateShort(stats.first_date);
        const last = formatDateShort(stats.last_date);
        document.getElementById('period-badge').textContent = `${first} — ${last}`;
    }
    
    // Color balance based on positive/negative
    const balanceEl = document.getElementById('net-balance');
    if (stats.net_balance >= 0) {
        balanceEl.style.color = '#10b981';
    } else {
        balanceEl.style.color = '#ef4444';
    }
}

function renderTrendsChart() {
    const ctx = document.getElementById('trends-chart').getContext('2d');
    const { trends } = dashboardData;
    
    if (trendsChart) {
        trendsChart.destroy();
    }
    
    const labels = trends.map(t => formatMonth(t.month));
    const incomeData = trends.map(t => t.income);
    const expenseData = trends.map(t => t.expenses);
    
    trendsChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels,
            datasets: [
                {
                    label: 'Receitas',
                    data: incomeData,
                    backgroundColor: 'rgba(16, 185, 129, 0.8)',
                    borderColor: '#10b981',
                    borderWidth: 1,
                    borderRadius: 4,
                    barPercentage: 0.6
                },
                {
                    label: 'Despesas',
                    data: expenseData,
                    backgroundColor: 'rgba(239, 68, 68, 0.8)',
                    borderColor: '#ef4444',
                    borderWidth: 1,
                    borderRadius: 4,
                    barPercentage: 0.6
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: {
                intersect: false,
                mode: 'index'
            },
            plugins: {
                legend: {
                    position: 'top',
                    labels: {
                        usePointStyle: true,
                        padding: 20
                    }
                },
                tooltip: {
                    backgroundColor: '#1c1c26',
                    titleColor: '#f0f0f5',
                    bodyColor: '#a0a0b0',
                    borderColor: '#2a2a38',
                    borderWidth: 1,
                    padding: 12,
                    callbacks: {
                        label: (ctx) => `${ctx.dataset.label}: ${formatCurrency(ctx.raw)}`
                    }
                }
            },
            scales: {
                x: {
                    grid: {
                        display: false
                    }
                },
                y: {
                    beginAtZero: true,
                    grid: {
                        color: '#2a2a38'
                    },
                    ticks: {
                        callback: (value) => formatCurrency(value, true)
                    }
                }
            }
        }
    });
}

function renderCategoriesChart() {
    const ctx = document.getElementById('categories-chart').getContext('2d');
    const { categories } = dashboardData;
    
    if (categoriesChart) {
        categoriesChart.destroy();
    }
    
    // Filter out income categories and sort by expenses
    const expenseCategories = Object.entries(categories)
        .filter(([key, val]) => val.expenses > 0 && !['salario', 'transferencias'].includes(key))
        .sort((a, b) => b[1].expenses - a[1].expenses)
        .slice(0, 8);  // Top 8
    
    const labels = expenseCategories.map(([key, val]) => val.display_name);
    const data = expenseCategories.map(([key, val]) => val.expenses);
    const colors = expenseCategories.map(([key]) => categoryColors[key]?.bg || '#6b7280');
    
    categoriesChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels,
            datasets: [{
                data,
                backgroundColor: colors,
                borderColor: '#1c1c26',
                borderWidth: 3,
                hoverOffset: 4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '65%',
            plugins: {
                legend: {
                    position: 'right',
                    labels: {
                        usePointStyle: true,
                        padding: 12,
                        font: { size: 11 }
                    }
                },
                tooltip: {
                    backgroundColor: '#1c1c26',
                    titleColor: '#f0f0f5',
                    bodyColor: '#a0a0b0',
                    borderColor: '#2a2a38',
                    borderWidth: 1,
                    callbacks: {
                        label: (ctx) => {
                            const total = ctx.dataset.data.reduce((a, b) => a + b, 0);
                            const pct = ((ctx.raw / total) * 100).toFixed(1);
                            return `${formatCurrency(ctx.raw)} (${pct}%)`;
                        }
                    }
                }
            }
        }
    });
}

function renderCategoriesGrid() {
    const { categories } = dashboardData;
    const grid = document.getElementById('categories-grid');
    
    // Calculate max expense for bar scaling
    const maxExpense = Math.max(...Object.values(categories).map(c => c.expenses || 0));
    
    // Sort by expenses
    const sorted = Object.entries(categories)
        .filter(([key, val]) => val.expenses > 0)
        .sort((a, b) => b[1].expenses - a[1].expenses);
    
    grid.innerHTML = sorted.map(([key, cat]) => {
        const pct = maxExpense > 0 ? (cat.expenses / maxExpense) * 100 : 0;
        const color = categoryColors[key]?.bg || '#6b7280';
        
        return `
            <div class="category-card">
                <div class="category-header">
                    <span class="category-name">${cat.display_name}</span>
                    <span class="category-count">${cat.count}</span>
                </div>
                <div class="category-amount">${formatCurrency(cat.expenses)}</div>
                <div class="category-bar">
                    <div class="category-bar-fill" style="width: ${pct}%; background: ${color}"></div>
                </div>
            </div>
        `;
    }).join('');
}

function populateCategoryFilter() {
    const select = document.getElementById('category-filter');
    const { categories } = dashboardData;
    
    Object.entries(categories)
        .sort((a, b) => a[1].display_name.localeCompare(b[1].display_name))
        .forEach(([key, cat]) => {
            const option = document.createElement('option');
            option.value = key;
            option.textContent = cat.display_name;
            select.appendChild(option);
        });
}

function filterTransactions() {
    const categoryFilter = document.getElementById('category-filter').value;
    const typeFilter = document.getElementById('type-filter').value;
    
    filteredTransactions = dashboardData.recent_transactions.filter(tx => {
        if (categoryFilter && tx.category !== categoryFilter) return false;
        if (typeFilter === 'debit' && tx.amount >= 0) return false;
        if (typeFilter === 'credit' && tx.amount < 0) return false;
        return true;
    });
    
    currentPage = 1;
    renderTransactions();
    renderPagination();
}

function renderTransactions() {
    const tbody = document.getElementById('transactions-body');
    
    const start = (currentPage - 1) * itemsPerPage;
    const end = start + itemsPerPage;
    const pageTransactions = filteredTransactions.slice(start, end);
    
    if (pageTransactions.length === 0) {
        tbody.innerHTML = `
            <tr>
                <td colspan="4" style="text-align: center; padding: 2rem; color: var(--text-muted);">
                    Nenhuma transação encontrada
                </td>
            </tr>
        `;
        return;
    }
    
    tbody.innerHTML = pageTransactions.map(tx => {
        const amountClass = tx.amount < 0 ? 'debit' : 'credit';
        const amountPrefix = tx.amount >= 0 ? '+' : '';
        
        return `
            <tr>
                <td class="tx-date">${formatDate(tx.date)}</td>
                <td class="tx-description" title="${escapeHtml(tx.description)}">${escapeHtml(tx.description)}</td>
                <td class="tx-category">${tx.category_display}</td>
                <td class="tx-amount ${amountClass} text-right">
                    ${amountPrefix}${formatCurrency(tx.amount)}
                </td>
            </tr>
        `;
    }).join('');
}

function renderPagination() {
    const pagination = document.getElementById('pagination');
    const totalPages = Math.ceil(filteredTransactions.length / itemsPerPage);
    
    if (totalPages <= 1) {
        pagination.innerHTML = '';
        return;
    }
    
    let html = `
        <button ${currentPage === 1 ? 'disabled' : ''} onclick="goToPage(${currentPage - 1})">
            ← Anterior
        </button>
        <span class="pagination-info">
            Página ${currentPage} de ${totalPages} 
            (${filteredTransactions.length} transações)
        </span>
        <button ${currentPage === totalPages ? 'disabled' : ''} onclick="goToPage(${currentPage + 1})">
            Próxima →
        </button>
    `;
    
    pagination.innerHTML = html;
}

function goToPage(page) {
    const totalPages = Math.ceil(filteredTransactions.length / itemsPerPage);
    if (page < 1 || page > totalPages) return;
    
    currentPage = page;
    renderTransactions();
    renderPagination();
    
    // Scroll to transactions section
    document.querySelector('.transactions-section').scrollIntoView({ 
        behavior: 'smooth',
        block: 'start'
    });
}

function updateLastUpdate() {
    const el = document.getElementById('last-update');
    if (dashboardData.exported_at) {
        el.textContent = formatDateTime(dashboardData.exported_at);
    }
}

// Utility functions
function formatCurrency(value, compact = false) {
    if (value === null || value === undefined) return '€0';
    
    const absValue = Math.abs(value);
    
    if (compact && absValue >= 1000) {
        return `€${(absValue / 1000).toFixed(1)}k`;
    }
    
    return new Intl.NumberFormat('pt-PT', {
        style: 'currency',
        currency: 'EUR',
        minimumFractionDigits: 0,
        maximumFractionDigits: 2
    }).format(absValue);
}

function formatDate(dateStr) {
    const date = new Date(dateStr);
    return date.toLocaleDateString('pt-PT', {
        day: '2-digit',
        month: 'short',
        year: 'numeric'
    });
}

function formatDateShort(dateStr) {
    const date = new Date(dateStr);
    return date.toLocaleDateString('pt-PT', {
        month: 'short',
        year: 'numeric'
    });
}

function formatMonth(monthStr) {
    const [year, month] = monthStr.split('-');
    const date = new Date(year, parseInt(month) - 1);
    return date.toLocaleDateString('pt-PT', {
        month: 'short',
        year: '2-digit'
    });
}

function formatDateTime(dateStr) {
    const date = new Date(dateStr);
    return date.toLocaleString('pt-PT', {
        day: '2-digit',
        month: 'short',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
