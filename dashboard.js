document.getElementById('apply-filters').addEventListener('click', function() {
    const filters = {
        end_year: document.getElementById('end_year').value,
        topics: document.getElementById('topics').value,
        sector: document.getElementById('sector').value,
        region: document.getElementById('region').value,
        pest: document.getElementById('pest').value,
        source: document.getElementById('source').value,
        swot: document.getElementById('swot').value,
        country: document.getElementById('country').value,
        city: document.getElementById('city').value,
    };

    let query = Object.keys(filters)
        .map(key => filters[key] ? `${key}=${filters[key]}` : '')
        .filter(param => param)
        .join('&');

    document.getElementById('loading').style.display = 'block';
    document.getElementById('error').style.display = 'none';
    document.getElementById('visualizations').innerHTML = '';

    fetch(`/data?${query}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('loading').style.display = 'none';
            updateVisualizations(data);
        })
        .catch(error => {
            document.getElementById('loading').style.display = 'none';
            document.getElementById('error').style.display = 'block';
            console.error('Error fetching data:', error);
        });
});

document.getElementById('clear-filters').addEventListener('click', function() {
    document.getElementById('end_year').value = '';
    document.getElementById('topics').value = '';
    document.getElementById('sector').value = '';
    document.getElementById('region').value = '';
    document.getElementById('pest').value = '';
    document.getElementById('source').value = '';
    document.getElementById('swot').value = '';
    document.getElementById('country').value = '';
    document.getElementById('city').value = '';
    document.getElementById('visualizations').innerHTML = '';
});

function updateVisualizations(data) {
    const svgWidth = 800;
    const svgHeight = 400;
    const margin = { top: 20, right: 30, bottom: 40, left: 90 };
    const width = svgWidth - margin.left - margin.right;
    const height = svgHeight - margin.top - margin.bottom;

    const svg = d3.select("#visualizations")
        .append("svg")
        .attr("width", svgWidth)
        .attr("height", svgHeight)
        .attr("viewBox", `0 0 ${svgWidth} ${svgHeight}`)
        .attr("preserveAspectRatio", "xMidYMid meet");

    const x = d3.scaleLinear().domain([0, d3.max(data, d => d.intensity)]).range([0, width]);
    const y = d3.scaleBand().domain(data.map(d => d.year)).range([0, height]).padding(0.1);

    const g = svg.append("g").attr("transform", `translate(${margin.left},${margin.top})`);

    g.append("g").selectAll("rect").data(data).enter().append("rect")
        .attr("x", 0)
        .attr("y", d => y(d.year))
        .attr("width", d => x(d.intensity))
        .attr("height", y.bandwidth())
        .attr("fill", "steelblue");

    g.append("g").call(d3.axisLeft(y));
    g.append("g").attr("transform", `translate(0,${height})`).call(d3.axisBottom(x));
}

