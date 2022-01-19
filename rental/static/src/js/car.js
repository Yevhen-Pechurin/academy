odoo.define('rental.car', function (require) {
    'use strict';

    const Engine = require('rental.engine');

    const Car = Engine.extend({
        volume: function () {
            this._super.apply(this, arguments);
        },
        maxspeed: function () {
            this.mspeed = 180;
            console.log('maxspeed', this.mspeed);
        },
    });
    const car = new Car();
    car.volume()
    car.maxspeed()
    return Car;
})