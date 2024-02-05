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
        .then((exchangeRates) => {
            console.log(exchangeRates)
            // Iteracja po danych z API i dodanie ich do bazy danych
            exchangeRates.forEach(rate => {
                let currencyCode = rate.currency_code;
                let rateValue = rate.rate_value;
                let currencyName = getCurrencyName(currencyCode);

                addToDatabase(currencyCode, currencyName, rateValue, selectedDate);
            });
        });
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
