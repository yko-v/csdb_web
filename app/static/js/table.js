async function loadTable(url) {
    const response = await fetch(url);
    const data = await response.json();

    const tableElement = document.getElementById("data-table");

    // Очистка если таблица уже инициализирована
    if ($.fn.DataTable.isDataTable('#data-table')) {
        $('#data-table').DataTable().destroy();
        tableElement.innerHTML = "";
    }

    // Создаем header
    const thead = document.createElement("thead");
    const headerRow = document.createElement("tr");

    data.columns.forEach(col => {
        const th = document.createElement("th");
        th.textContent = col;
        headerRow.appendChild(th);
    });

    thead.appendChild(headerRow);
    tableElement.appendChild(thead);

    // Создаем body
    const tbody = document.createElement("tbody");

    data.rows.forEach(row => {
        const tr = document.createElement("tr");
        row.forEach(cell => {
            const td = document.createElement("td");
            td.textContent = cell !== null ? cell : "";
            tr.appendChild(td);
        });
        tbody.appendChild(tr);
    });

    tableElement.appendChild(tbody);

    // Инициализация DataTables
    $('#data-table').DataTable({
        pageLength: 25,
        lengthMenu: [10, 25, 50, 100],
        ordering: true,
        searching: true,
        info: true,
        language: {
            search: "Поиск:",
            lengthMenu: "Показывать _MENU_",
            info: "Показано _START_–_END_ из _TOTAL_",
            paginate: {
                previous: "Назад",
                next: "Вперёд"
            }
        }
    });

    document.getElementById("total-count").textContent = data.rows.length;
}

