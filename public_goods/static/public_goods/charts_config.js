/**
 * Centralized configuration for Highcharts graphs.
 */
const ChartsConfig = {
    common: {
        credits: { enabled: false },
        exporting: { enabled: true },
        legend: { enabled: true },
        responsive: {
            rules: [{
                condition: { maxWidth: 500 },
                chartOptions: { legend: { enabled: false } }
            }]
        }
    },
    axes: {
        yAxis: function (max) {
            return {
                title: { text: 'Tokens' },
                min: 0,
                max: max,
                tickInterval: 5
            };
        },
        xAxis: function (numRounds) {
            return {
                title: { text: 'Round' },
                type: 'linear',
                min: 1,
                max: numRounds,
                tickInterval: 1,
                labels: { align: 'center' }
            };
        }
    },
    totalGroupChart: {
        chart: { type: 'line', height: 500 },
        title: { text: '' },
        tooltip: { headerFormat: 'Round {point.x}<br />', pointFormat: '{series.name}: {point.y:.0f} tokens' }
    },
    individualChart: {
        chart: { type: 'line', height: 400 },
        tooltip: { headerFormat: 'Round {point.x}<br />', pointFormat: '{series.name}: {point.y:.0f} tokens' }
    },
    colors: [
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
        '#9467bd', '#8c564b', '#e377c2', '#7f7f7f'
    ]
};

