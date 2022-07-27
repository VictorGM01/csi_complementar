// Gráfico de pizza 3D

google.charts.load("current", {packages:["corechart"]});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
    var data = google.visualization.arrayToDataTable([
      ['Alternativa', 'Resposta'],
      ["", 1]  // exemplo
    ]);

    var options = {
      title: 'Nome da questão',
      is3D: true,  // Gráfico 3d
      colors: ["RGB das cores, na ordem dos dados"],
      backgroundColor: "transparent",

      // Descomentar este código se o gráfico tiver explosão
      // pieSliceText: 'label',
      // slices: {num. da label: {offset: 0.2}},
    };

    var chart = new google.visualization.PieChart(document.getElementById('perguntaX'));
    chart.draw(data, options);
}

// Gráfico de Colunas

google.charts.load("current", {packages:["corechart"]});
    google.charts.setOnLoadCallback(drawChart14);
    function drawChart14() {
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Questao');
    data.addColumn('number', 'Respostas');
    data.addRows([
      ["Sim", 1], // exemplo
    ]);

    var options = {
      colors: [''],  // cor das colunas
      bars: 'vertical',
      backgroundColor: "#4a8450",
      legend: "none",
    };

    var chart = new google.visualization.ColumnChart(document.getElementById('perguntaXY'));
    chart.draw(data, options);
}

// Gráfico de barras

google.charts.load("current", {packages:["corechart"]});
    google.charts.setOnLoadCallback(drawChart7);
    function drawChart7() {
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Questao');
    data.addColumn('number', 'Respostas');
    data.addRows([
      ["Sim", 1],  // exemplo de linha
    ]);

    var options = {
      colors: [''], // cor das linhas
      bars: 'horizontal',
      backgroundColor: "#4a8450",
      legend: "none",
    };

    var chart = new google.visualization.BarChart(document.getElementById('perguntaXYZ'));
    chart.draw(data, options);
}
