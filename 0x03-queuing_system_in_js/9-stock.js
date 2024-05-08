const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const listProducts = [
  {Id: 1, name: 'Suitcase 250', price: 50, stock: 4},
  {Id: 2, name: 'Suitcase 450', price: 100, stock: 10},
  {Id: 3, name: 'Suitcase 650', price: 350, stock: 2},
  {Id: 4, name: 'Suitcase 1050', price: 550, stock: 0}
]

function getItemById(id) {
  for (const product of listProducts) {
    if (product.Id === id) {
      return product;
    }
  }
  return null
}

const client = redis.createClient();

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
}).on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

function getCurrentReservedStockById(itemId, callback) {
  client.get(`item.${itemId}`, (err, reply) => {
    if (err) {
      callback(err);
    } else {
      callback(null, reply)
    }
  });

}
const getReserveStock = promisify(getCurrentReservedStockById);

const app = express();

app.get('/list_products', (req, res) => {
  res.send(listProducts);
});

app.get('/list_products/:itemId', (req, res) => {
  const itemId = +req.params.itemId;

  getReserveStock(itemId, (error, reply) => {
    if (error || reply == null) {
      res.send({"status":"Product not found"});
    } else {
      res.send(reply);
    }
  });
});

app.get('/reserve_product/:itemId', (req, res) => {
 const id = +req.params.itemId;

 const value = getItemById(id);
 
 if (value === null) {
  return res.send({"status":"Product not found"});
 }

 if (value['stock'] <= 0) {
   res.send({"status":"Not enough stock available","itemId":id});
 }

 reserveStockById(id, JSON.stringify(value));

 res.send({"status":"Reservation confirmed","itemId":id});
});

app.listen(1245, () => {
  console.log('Server listining on port 1245');
});
