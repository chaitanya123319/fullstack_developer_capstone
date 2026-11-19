const express = require('express');
const mongoose = require('mongoose');
const fs = require('fs');
const path = require('path');
const cors = require('cors');

const Reviews = require('./review');
const Dealerships = require('./dealership');

const app = express();
const port = process.env.PORT || 3030;
const mongoUrl = process.env.MONGO_URL || 'mongodb://mongo_db:27017/';

app.use(cors());
app.use(express.json());

const readJson = (name) =>
  JSON.parse(fs.readFileSync(path.join(__dirname, 'data', name), 'utf8'));

const escapeRegex = (text) => text.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

// Load the sample data the first time the collections are empty.
async function seedDatabase() {
  if ((await Dealerships.countDocuments()) === 0) {
    await Dealerships.insertMany(readJson('dealerships.json').dealerships);
  }
  if ((await Reviews.countDocuments()) === 0) {
    await Reviews.insertMany(readJson('reviews.json').reviews);
  }
}

app.get('/', (req, res) => {
  res.send('Welcome to the Dealership API');
});

// All reviews
app.get('/fetchReviews', async (req, res) => {
  try {
    res.json(await Reviews.find());
  } catch (error) {
    res.status(500).json({ error: 'Error fetching reviews' });
  }
});

// Reviews for one dealer
app.get('/fetchReviews/dealer/:id', async (req, res) => {
  try {
    res.json(await Reviews.find({ dealership: parseInt(req.params.id, 10) }));
  } catch (error) {
    res.status(500).json({ error: 'Error fetching dealer reviews' });
  }
});

// All dealers
app.get('/fetchDealers', async (req, res) => {
  try {
    res.json(await Dealerships.find());
  } catch (error) {
    res.status(500).json({ error: 'Error fetching dealers' });
  }
});

// Dealers in one state, e.g. /fetchDealers/Kansas
app.get('/fetchDealers/:state', async (req, res) => {
  try {
    const state = new RegExp(`^${escapeRegex(req.params.state)}$`, 'i');
    res.json(await Dealerships.find({ state }));
  } catch (error) {
    res.status(500).json({ error: 'Error fetching dealers by state' });
  }
});

// One dealer by id, e.g. /fetchDealer/1
app.get('/fetchDealer/:id', async (req, res) => {
  try {
    res.json(await Dealerships.find({ id: parseInt(req.params.id, 10) }));
  } catch (error) {
    res.status(500).json({ error: 'Error fetching dealer' });
  }
});

// Add a review
app.post('/insert_review', async (req, res) => {
  try {
    const data = req.body;
    const last = await Reviews.findOne().sort({ id: -1 });
    const review = new Reviews({
      id: last ? last.id + 1 : 1,
      name: data.name,
      dealership: data.dealership,
      review: data.review,
      purchase: data.purchase,
      purchase_date: data.purchase_date,
      car_make: data.car_make,
      car_model: data.car_model,
      car_year: data.car_year
    });
    res.json(await review.save());
  } catch (error) {
    res.status(500).json({ error: 'Error inserting review' });
  }
});

async function start() {
  await mongoose.connect(mongoUrl, { dbName: 'dealershipsDB' });
  await seedDatabase();
  app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
  });
}

start().catch((error) => {
  console.error('Failed to start server:', error.message);
  process.exit(1);
});
