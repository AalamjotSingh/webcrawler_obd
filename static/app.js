document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/links')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector('#linksTable tbody');
            data.forEach(link => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td><a href="${link.link}" target="_blank">${link.link}</a></td>
                    <td>${new Date(link.dateScraped).toLocaleString()}</td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(err => console.error('Error fetching links:', err));
});
