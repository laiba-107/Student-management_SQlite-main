// Global Variables
let currentPage = 1;
const itemsPerPage = 10;

// DOM Ready
document.addEventListener('DOMContentLoaded', function() {
    // Initialize all modules
    initNavigation();
    initModals();
    initSearch();
    initStudentManagement();
    initCourseManagement();
    initDepartmentManagement();
    initInstructorManagement();
    initEnrollmentManagement();
    initAnalytics();
    initPasswordChange();
});

// Initialize Navigation
function initNavigation() {
    // Highlight active navigation item
    const currentPath = window.location.pathname.split('/').pop() || 'dashboard';
    document.querySelectorAll('.sidebar nav ul li').forEach(item => {
        if (item.getAttribute('data-section') === currentPath) {
            item.classList.add('active');
        }
    });
}

// Initialize Modals
function initModals() {
    // Generic modal handling
    const modals = document.querySelectorAll('.modal');
    const modalTriggers = document.querySelectorAll('[data-modal-target]');
    const closeButtons = document.querySelectorAll('.close-modal, .modal .btn-outline');
    
    modalTriggers.forEach(trigger => {
        trigger.addEventListener('click', () => {
            const modalId = trigger.getAttribute('data-modal-target');
            document.getElementById(modalId).style.display = 'block';
        });
    });
    
    closeButtons.forEach(button => {
        button.addEventListener('click', () => {
            modals.forEach(modal => modal.style.display = 'none');
        });
    });
    
    window.addEventListener('click', (e) => {
        if (e.target.classList.contains('modal')) {
            e.target.style.display = 'none';
        }
    });
}

// Initialize Global Search
function initSearch() {
    const searchInput = document.getElementById('global-search');
    const searchResults = document.getElementById('search-results');
    
    searchInput.addEventListener('input', debounce(function() {
        const query = this.value.trim();
        if (query.length < 2) {
            searchResults.style.display = 'none';
            return;
        }
        
        fetch(`/api/search?q=${encodeURIComponent(query)}`)
            .then(res => res.json())
            .then(data => {
                let html = '';
                
                if (data.students.length > 0) {
                    html += '<div class="search-category"><h4>Students</h4><ul>';
                    data.students.forEach(student => {
                        html += `
                            <li>
                                <a href="/students#${student.id}">
                                    ${student.name} (${student.email})
                                </a>
                            </li>
                        `;
                    });
                    html += '</ul></div>';
                }
                
                if (data.courses.length > 0) {
                    html += '<div class="search-category"><h4>Courses</h4><ul>';
                    data.courses.forEach(course => {
                        html += `
                            <li>
                                <a href="/courses#${course.id}">
                                    ${course.name} (${course.code})
                                </a>
                            </li>
                        `;
                    });
                    html += '</ul></div>';
                }
                
                if (html) {
                    searchResults.innerHTML = html;
                    searchResults.style.display = 'block';
                } else {
                    searchResults.style.display = 'none';
                }
            });
    }, 300));
    
    // Hide results when clicking outside
    document.addEventListener('click', (e) => {
        if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
            searchResults.style.display = 'none';
        }
    });
}

// Debounce function for search
function debounce(func, wait) {
    let timeout;
    return function() {
        const context = this, args = arguments;
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(context, args), wait);
    };
}

// Initialize Student Management
function initStudentManagement() {
    if (!document.getElementById('students-table')) return;
    
    // Load initial data
    loadStudents();
    loadDepartmentsForSelect('#department, #department-filter');
    
    // Add event listeners
    document.getElementById('add-student-btn').addEventListener('click', showAddStudentModal);
    document.getElementById('student-form').addEventListener('submit', handleStudentFormSubmit);
    document.getElementById('department-filter').addEventListener('change', loadStudents);
    document.getElementById('status-filter').addEventListener('change', loadStudents);
    document.getElementById('reset-filters').addEventListener('click', resetFilters);
    document.getElementById('prev-page').addEventListener('click', goToPrevPage);
    document.getElementById('next-page').addEventListener('click', goToNextPage);
}

function loadStudents() {
    const departmentFilter = document.getElementById('department-filter').value;
    const statusFilter = document.getElementById('status-filter').value;
    
    let url = `/api/students?page=${currentPage}&limit=${itemsPerPage}`;
    if (departmentFilter) url += `&department_id=${departmentFilter}`;
    if (statusFilter) url += `&status=${statusFilter}`;
    
    fetch(url)
        .then(res => res.json())
        .then(data => {
            renderStudentsTable(data.students);
            updatePagination(data.total, data.page, data.pages);
        });
}

// Add similar initialization functions for other entities (courses, departments, etc.)

// Initialize Analytics Dashboard
function initAnalytics() {
    if (!document.getElementById('analytics-section')) return;
    
    fetch('/api/analytics')
        .then(res => res.json())
        .then(data => {
            renderStudentStatsChart(data.student_stats);
            renderGradeDistributionChart(data.grade_stats);
            renderEnrollmentTrendChart(data.enrollment_trend);
        });
}

// Helper function to show toast messages
function showToast(message, type = 'success') {
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.textContent = message;
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.classList.add('show');
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 300);
        }, 3000);
    }, 100);
}

// Add all other necessary functions for complete functionality