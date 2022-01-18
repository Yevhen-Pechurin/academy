odoo.define('zoom_info.animal', function (require) {
    'use strict';

    const Class = require('web.Class');

    const Animal = Class.extend({
        init: function () {
            this.x = 0;
            this.hunger = 0;
        },
        move: function () {
            this.x = this.x + 1;
            this.hunger = this.hunger + 1;
            console.log('move', this.x, this.hunger);
        },
        eat: function () {
            this.hunger = 0;
        },
    });

    const Widget = require('web.Widget');

    const Counter = Widget.extend({
        template: 'zoom_info.zoom_info_template',
        events: {
            'click .increment_btn': '_onClick',
            'click .start_timer': '_startTimer',
        },
        init: function (parent, value) {
            this._super(parent);
            this.count = value;
        },
        _onClick: function () {
            this.count++;
            this.$('.val').text(this.count);
        },
        _startTimer: function () {
            setInterval(() => {
                this.count++;
                this.$('.val').text(this.count);
            }, 1000)
        }
    });
    require('web.dom_ready')
    var counter = new Counter(this, 4);
// Render and insert into DOM
    counter.appendTo("body");

    // return Animal;
})