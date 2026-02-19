async function loadOrbits() {
    const parameter = document.getElementById("param").value;
    const family = document.getElementById("family").value;

    const response = await fetch(
        `/api/orbits?norad_id=${norad}&parameter=${parameter}`
    );

    const data = await response.json();

    const grouped = {};

    data.data.forEach(row => {
        const norad = row[0];
        const date = row[1];
        const value = row[2];

        if (!grouped[norad]) {
            grouped[norad] = { x: [], y: [] };
        }

        grouped[norad].x.push(date);
        grouped[norad].y.push(value);
    });

    const traces = Object.keys(grouped).map(norad => ({
        x: grouped[norad].x,
        y: grouped[norad].y,
        mode: "lines",
        name: norad
    }));

    Plotly.newPlot("orbitChart", traces);
}
async function loadOrbits() {
    const norad = document.getElementById("norad_id").value;
    const parameter = document.getElementById("parameter").value;

    const response = await fetch(
        `/api/orbits?norad_id=${norad}&parameter=${parameter}`
    );

    const data = await response.json();

    console.log(data);   // ← ВАЖНО

    drawChart(data);
}

