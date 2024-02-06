document.getElementById('ActualExchangeRateButton').addEventListener('click',function (){
    document.getElementById('hiddenCurrencyTable').style.visibility = 'visible'

    document.getElementById('ActualExchangeRateBody').innerHTML =``

    fetch('/api/actual_RON_rate')
        .then(response => response.json())
        .then((exchangeRates)=>{
            console.log(exchangeRates)
            exchangeRates.forEach(Rate =>{
                currency_code = Rate[1];
                currency_name = Rate[2];
                rate_value = Rate[3];
                date_time = Rate[4];

                document.getElementById('ActualExchangeRateBody').innerHTML +=`
                    <tr>
                        <td>${currency_code}</td>
                        <td>${currency_name}</td>
                        <td>${rate_value}</td>
                        <td>${date_time}</td>
                    </tr>
                `
            })


        })
})