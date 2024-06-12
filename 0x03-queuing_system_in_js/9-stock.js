import express from "express";
import { createClient, print } from 'redis'
import { promisify } from 'util';

const app = express();
const client = createClient();
client.get = promisify(client.get);

let listProducts = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5
  }
]

function reserveStockById(itemId, stock) {
  client.set(itemId, stock, print);
}

async function getCurrentReservedStockById(itemId) {
  const value = await client.get(itemId);
  return value; 
}

function getItemById(id) {
  return listProducts.find(product => String(product.id) === id);
}

app.get('/list_products', (req, res) => {
  const newListProducts = []
  listProducts.forEach(product => {
    newListProducts.push({
      "itemId": product.id,
      "itemName": product.name,
      "price":product.price,
      "initialAvailableQuantity": product.stock
    })
  })
  res.json(newListProducts);
})

app.get('/list_products/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const product =  await getCurrentReservedStockById(itemId);

  if (!product) {
    return res.json({"status":"Product not found"})
  }

  res.json(JSON.parse(product))
})

app.get('/reserve_product/:itemId', (req, res) => {
  let { itemId } = req.params;
  const product = getItemById(itemId)
  if (!product) {
    return res.json({"status":"Product not found"});
  }
  const inStock = product.stock;
  if (inStock < 1) {
    return res.json({"status":"Not enough stock available","itemId":itemId})
  }
  reserveStockById(itemId, JSON.stringify(
    {"itemId": product.id,"itemName":product.name,"price":product.price,"initialAvailableQuantity":product.stock,"currentQuantity":product.stock}
  ))
  listProducts = listProducts.map(prod => {
    if (String(prod.id) === itemId) {
      return {...prod, stock: prod.stock - 1}
    }
    return prod
  })
  res.json({"status":"Reservation confirmed","itemId": itemId})
})

app.listen(1245, () => console.log('server running on port 1245'));
