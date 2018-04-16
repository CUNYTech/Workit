var http = require('http');


http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write("Hello" );
    res.end();
}).listen(8080);


const ccxt = require ('ccxt');


(async () => {
	let exchange = new ccxt.coinmarketcap();
    console.log (await (exchange.fetchTicker ('BTC/USD'))) // ticker for BTC/USD
    let symbols = Object.keys (exchange.markets)
    let random = Math.floor ((Math.random () * symbols.length)) - 1
    console.log (exchange.fetchTicker (symbols[random])) // ticker for a random symbol
}) ();


(async () => {
	let exchange = new ccxt.coinmarketcap();
    console.log (await (exchange.fetchGlobal())); // all tickers indexed by their symbols
}) ();


// (async () => {
// 	 let kraken = new ccxt.kraken ()
//     let pairs = await kraken.publicGetSymbolsDetails ()
//     let marketIds = Object.keys (pairs['result'])
//     let marketId = marketIds[0]
//     let ticker = await kraken.publicGetTicker ({ pair: marketId })
//     console.log (kraken.id, marketId, ticker)
// }) ();

// (async () => {

//     console.log (await exchange.loadMarkets ())

//     let btcusd1 = exchange.markets['BTC/USD']     // get market structure by symbol
//     let btcusd2 = exchange.market ('BTC/USD')     // same result in a slightly different way

//     let btcusdId = exchange.marketId ('BTC/USD')  // get market id by symbol

//     let symbols = exchange.symbols                // get an array of symbols
//     let symbols2 = Object.keys (exchange.markets) // same as previous line

//     console.log (exchange.id, symbols)            // print all symbols

//     let currencies = exchange.currencies          // a list of currencies

//     let bitfinex = new ccxt.bitfinex ()
//     await bitfinex.loadMarkets ()

//     bitfinex.markets['BTC/USD']                   // symbol → market (get market by symbol)
//     bitfinex.markets_by_id['XRPBTC']              // id → market (get market by id)

//     bitfinex.markets['BTC/USD']['id']             // symbol → id (get id by symbol)
//     bitfinex.markets_by_id['XRPBTC']['symbol']    // id → symbol (get symbol by id)

// });
