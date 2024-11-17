const chartInstances = {};

// const line_chart = (res, canvas_id) => {
//     if (chartInstances[canvas_id]) {
//         chartInstances[canvas_id].destroy();
//     }
//
//     const canvas = $(`#${canvas_id}`);
//     const ctxLine = canvas[0].getContext('2d');
//     const config = {
//         type: 'line',
//         data: {
//             labels: res.labels,
//             datasets: [
//                 {
//                     type: 'scatter',
//                     label: 'Balance Checks',
//                     data: res.data_balance_check,
//                     borderWidth: 2,
//                     backgroundColor: 'rgba(28, 200, 138, 0.1)',
//                     borderColor: 'rgba(28, 200, 138, 1)',
//                 },
//                 {
//                     type: 'scatter',
//                     label: 'Balance Today',
//                     data: res.data_today,
//                     borderWidth: 2,
//                     backgroundColor: 'rgba(246, 194, 62, 0.1)',
//                     borderColor: 'rgba(246, 194, 62, 1)',
//                 },
//                 {
//                     label: 'Balance Estimated',
//                     data: res.data_estimated,
//                     fill: true,
//                     borderWidth: 2,
//                     backgroundColor: "rgba(78, 115, 223, 0.1)",
//                     borderColor: "rgba(78, 115, 223, 1)",
//                     cubicInterpolationMode: 'monotone',
//                     tension: 0.4,
//                     pointRadius: 0,
//                 },
//             ]
//         },
//         options: {
//             maintainAspectRatio: false,
//             layout: {
//                 padding: {
//                     left: 10,
//                     right: 10,
//                     top: 10,
//                     bottom: 5
//                 }
//             },
//             responsive: true,
//             plugins: {
//                 legend: {
//                     position: 'top',
//                 },
//                 title: {
//                     display: false,
//                 },
//                 tooltip: {
//                     mode: 'index',
//                     intersect: false,
//                     position: 'nearest'
//                 }
//             },
//             elements: {
//                 point: {
//                     radius: 4,
//                 }
//             },
//             scales: {
//                 x: {
//                     grid: {
//                         display: false,
//                         drawBorder: false
//                     },
//                     ticks: {
//                         display: true,
//                         autoSkip: true
//                     }
//                 },
//                 y: {
//                     ticks: {
//                         maxTicksLimit: 5,
//                         padding: 10,
//                         // Include a dollar sign in the ticks
//                         callback: function (value, index, values) {
//                             return new Intl.NumberFormat('en-IE', {
//                                 style: 'currency', currency: 'USD',
//                                 maximumSignificantDigits: 1
//                             }).format(value);
//                         }
//                     },
//                     gridLines: {
//                         color: "rgb(234, 236, 244)",
//                         zeroLineColor: "rgb(234, 236, 244)",
//                         drawBorder: false,
//                         borderDash: [2],
//                         zeroLineBorderDash: [2]
//                     }
//                 },
//             }
//         }
//     };
//     chartInstances[canvas_id] = new Chart(ctxLine, config);
//
//     return chartInstances[canvas_id];
// }

const doughnut_chart = (res, canvas_id) => {
    if (chartInstances[canvas_id]) {
        chartInstances[canvas_id].destroy();
    }

    const canvas = $(`#${canvas_id}`);
    const ctxDoughnut = canvas[0].getContext('2d');
    const config = {
        type: 'doughnut',
        data: {
            labels: res.labels,
            datasets: [
                {
                    data: res.data,
                    backgroundColor: [
                        'rgb(255, 99, 132)',
                        'rgb(255, 159, 64)',
                        'rgb(255, 205, 86)',
                        'rgb(75, 192, 192)',
                        'rgb(54, 162, 235)',
                        'rgb(153, 102, 255)',
                        'rgb(201, 203, 207)',
                        'rgb(234,21,28)',
                        'rgb(20,143,121)',
                        'rgb(14,232,22)',
                    ],
                    hoverOffset: 4,
                }
            ]
        },
        options: {
            maintainAspectRatio: false,
            layout: {
                padding: {
                    left: 5,
                    right: 5,
                    top: 5,
                    bottom: 5
                }
            },
            responsive: true,
            plugins: {
                tooltip: {
                    callbacks: {
                        label: function (context) {
                            const label = context.label || '';
                            const value = parseFloat(context.raw) || 0;
                            const total = context.dataset.data
                                .reduce((sum, val) => sum + (parseFloat(val) || 0), 0);
                            const percentage = total > 0 ? ((value / total) * 100) : 0;

                            return `${label}: $${value.toLocaleString()} (${percentage.toFixed(1)}%)`;
                        }
                    }
                }
            }
        },
    };
    chartInstances[canvas_id] = new Chart(ctxDoughnut, config);

    return chartInstances[canvas_id];
}