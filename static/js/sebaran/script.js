const sebaran_values = document.currentScript.getAttribute('data-sebaran-values').replace(/'/g, '"');
const sebaran_data = JSON.parse(sebaran_values);

let d_labels = []
let d_data_aktif = []

for (let i=0; i<sebaran_data.length; i++) {
    d_labels.push(sebaran_data[i].provinsi)
    d_data_aktif.push(sebaran_data[i].jumlah_kasus_aktif)
}

const ctx = document.getElementById('sebaranChart').getContext('2d');
const chart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: d_labels,
        datasets: [
            {
                label: 'Jumlah Kasus Aktif per Provinsi',
                data: d_data_aktif,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            },
        ]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});