odoo.define('rental.car_interface', function(require) {
    'use strict';

    //const Class = require('web.Class');
    const Widget = require('web.Widget');

    const ManualGearboxMixin = {
        gear: 0,
        reverse: function() {
            if (this.gear === 'neutral') {
                this.gear = 'reverse';
                console.log("You've shifted to reverse gear.")
            } else {
                console.log('Before shifting to reverse gear, first stop the car.')
            }
        },
        neutral: function() {
            this.gear = 'neutral';
            console.log("You've shifted to neutral gear.")
        },
        downshift: function() {
            if (this.gear === 'neutral' | this.gear === 'reverse') return false;
            if (this.gear === 1) {
                this.neutral();
            } else {
                this.gear--;
            }
            console.log(`You've downshifted to ${this.gear} gear.`);
        },
        upshift: function() {
            if (this.gear === 'neutral' | this.gear === 'reverse') {
                this.gear = 1;
            } else if (this.gear < 6) {
                this.gear++;
            } else {
                console.log('This vehicle has only 6 gears.')
            }
            console.log(`You've upshifted to ${this.gear} gear.`);
        }
    };

    const Vehicle = Widget.extend({
        engineStarted: false,
        isMoving: false,
        init: () => {},
        startEngine: function() {
            if (this.engineStarted) {
                console.log('The engine is already started.');
                return false;
            }
            this.engineStarted = true;
            console.log('The engine has started.');
        },
        accelarate: function() {
            if (!this.engineStarted) {
                console.log('First start the engine.');
                return false;
            }
            this.isMoving = true;
            console.log("You're speading up.");
        },
        brake: function() {
            if (this.isMoving) {
                console.log("You're slowing down.");
            }
        },
        stopCar: function() { 
            setTimeout(() => {
                console.log("The car is stopped.");
                this.isMoving = false;
            }, 1000);
        },
        stopEngine: function() {
            if (this.engineStarted) {
                this.engineStarted = false;
                console.log("You've stopped the engine.");
            }
        },
    });

    const ManualCar = Vehicle.extend(ManualGearboxMixin, {
        template: 'car_interface_template',
        events: {
            'click #start_engine_btn': 'startEngine',
            'click #accelarate_btn': 'accelarate',
            'click #brake_btn': 'brake',
            'click #stop_engine_btn': 'stopEngine',
        },
    });

    ManualCar.include({
        events: _.extend({}, ManualCar.events, {
            'click #stop_btn': 'stopCar',
            'click #upshift_btn': 'upshift',
            'click #downshift_btn': 'downshift',
            'click #reverse_gear_btn': 'reverse',
            'click #neutral_gear_btn': 'neutral',
        }),
        _displayGear: function() {
            $('.val').text(`Current gear: ${this.gear}`);
        },
        stopCar: function() {
            this.gear = 'neutral';
            this._displayGear();
            this._super();
        },
        downshift: function() {
            this._super();
            this._displayGear();
        },
        upshift: function() {
            this._super();
            this._displayGear();
        },
        neutral: function() {
            this._super();
            this._displayGear();
        },
        reverse: function() {
            this._super();
            this._displayGear();
        },
    });

    require('web.dom_ready');
    const car = new ManualCar();
    car.appendTo("body");
})