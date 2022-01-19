odoo.define('rental.engine', function (require) {
    'use strict';

    const Class = require('web.Class');

    const Engine = Class.extend({
        volume: function () {
            this.v = 1598;
            console.log('volume', this.v);
        },
        fuel: function () {
            this.fuel = 'petrol';
            console.log('fuel', this.fuel);
        },
    });
    const engine = new Engine()
    engine.volume()
    engine.fuel()
    return Engine;
})