var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: "Wegman's Wild Workout on the World Wide Web..." });
});

module.exports = router;
