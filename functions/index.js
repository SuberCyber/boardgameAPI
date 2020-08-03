const functions = require('firebase-functions');
const admin = require('firebase-admin');
const express = require('express');
const cors = require('cors');
const app = express();
app.use(cors({ origin: true }));
const list = require('./formatting/listOfGamesInfo.json');

app.get('/', (req, res) => {
  return res.status(200).send(list);
});

exports.app = functions.https.onRequest(app);