const currencyNames = {
    'EUR': 'Euro',
    'USD': 'Dolar Amerykański',
    'CHF': 'Frank Szwajcarski',
    'CNY': 'Renminbi chińskie',
    'CAD': 'Dolar Kanadyjski',
    'CZK': 'Korona Czeska',
    'EGP': 'Funt Egipski',
    'PLN': 'Polski Złoty',
    'SEK': 'Korona Szwedzka',
    'GBP': 'Funt Brytyjski',
};

function getCurrencyName(currencyCode) {
    return currencyNames[currencyCode] || 'Unknown';
}

document.getElementById('getExchangeRateButton').addEventListener('click', function () {
    document.getElementById('hiddenCurrencyTable').style.visibility = 'visible';
    document.getElementById('ActualExchangeRateBody').innerHTML =``

    // We get Date Here
    let selectedDate = document.getElementById('dateInput').value; // załóżmy, że masz pole input z id='dateInput'

    // We contact Outside API here to get Exchange rate for RON
    let apiUrl = `https://api.currencyapi.com/v3/historical?apikey=cur_live_mJ4ACx3qhR78ONOpAXzXbIRTkxGcqcvADkJmPh75&currencies=EUR%2CUSD%2CCHF%2CCNY%2CCAD%2CCZK%2CEGP%2CPLN%2CSEK%2CGBP&base_currency=RON&date=${selectedDate}`;

    fetch(apiUrl)
        .then(response => response.json())
        .then((data) => {
        const exchangeRates = data.data;

        Object.keys(exchangeRates).forEach(currencyCode => {
            let rate = exchangeRates[currencyCode];
            let rateValue = rate.value;
            let currencyName = getCurrencyName(currencyCode);

            addToDatabase(currencyCode, currencyName, rateValue, selectedDate);
        });
        fillTableBasedOnDate(selectedDate);
    })

});

document.getElementById('ActualExchangeRateButton').addEventListener('click', function () {
    document.getElementById('hiddenCurrencyTable').style.visibility = 'visible';
    document.getElementById('ActualExchangeRateBody').innerHTML =``

    let today = new Date();
    let year = today.getFullYear();
    let month = String(today.getMonth() + 1).padStart(2, '0');
    let day = String(today.getDate()).padStart(2, '0');
    let currentDate = `${year}-${month}-${day}`;

    // We contact Outside API here to get Exchange rate for RON
    let apiUrl = `https://api.currencyapi.com/v3/latest?apikey=cur_live_mJ4ACx3qhR78ONOpAXzXbIRTkxGcqcvADkJmPh75&currencies=EGP%2CGBP%2CCZK%2CEUR%2CUSD%2CCHF%2CSEK%2CPLN%2CCNY%2CCAD&base_currency=RON`;

    fetch(apiUrl)
        .then(response => response.json())
        .then((data) => {
        const exchangeRates = data.data;

        Object.keys(exchangeRates).forEach(currencyCode => {
            let rate = exchangeRates[currencyCode];
            let rateValue = rate.value;
            let currencyName = getCurrencyName(currencyCode);

            addToDatabase(currencyCode, currencyName, rateValue, currentDate);
        });
        fillTableBasedOnDate(currentDate);
    })

});

// Funkcja do dodawania danych do bazy danych
function addToDatabase(currencyCode, currencyName, rateValue, date) {
    fetch('/api/add_to_database', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            currency_code: currencyCode,
            currency_name: currencyName,
            rate_value: rateValue,
            date_time: date
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to add data to database');
        }
        return response.json();
    })
    .then(data => {
        console.log('Data added to database:', data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function fillTableBasedOnDate(date) {
    fetch('/api/fill_table_based_on_date', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            date: date
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to fill table based on date');
        }
        return response.json();
    })
    .then(data => {
    console.log('Table filled based on date:', data);

    data.forEach(rate => {
        let currency_code = rate.currency_code;
        let currency_name = rate.currency_name;
        let rate_value = rate.rate_value;
        let date_time = rate.date_time;

        document.getElementById('ActualExchangeRateBody').innerHTML += `
            <tr>
                <td>${currency_code}</td>
                <td>${currency_name}</td>
                <td>${rate_value}</td>
                <td>${date_time}</td>
            </tr>
        `;
    });
})
    .catch(error => {
        console.error('Error:', error);
    });
}
