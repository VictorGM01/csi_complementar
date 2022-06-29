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

    var chart = new google.visualization.PieChart(document.getElementById('piechart_3d'));
    chart.draw(data, options);
}