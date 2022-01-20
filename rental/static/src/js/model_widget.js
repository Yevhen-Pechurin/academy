odoo.define('rental.model_widget', function (require) {
    'use strict';

    const Widget = require('web.Widget');

    const Counter = Widget.extend({
        template: 'rental.rental_template',
        events: {
            'click button': '_onClick',
        },
        init: function (parent, value) {
            this._super(parent);
            this.count = value;
        },
        _onClick: function () {
            this.count++;
            this.$('.val').text(this.count);
        },
    });
    const counter = new Counter(this, 4);
    counter.appendTo("body");

})
// fieldRegistry.add('counter_widget', CounterWidget);


// odoo.define('rental.dog', function (require) {
//     'use strict';

//     const Widget = require('web.Widget');
//
//     const Counter = Widget.extend({
//         template: 'zoom_info.zoom_info_template',
//         events: {
//             'click .increment_btn': '_onClick',
//             'click .start_timer': '_startTimer',
//         },
//         init: function (parent, value) {
//             this._super(parent);
//             this.count = value;
//         },
//         _onClick: function () {
//             this.count++;
//             this.$('.val').text(this.count);
//         },
//         _startTimer: function () {
//             setInterval(() => {
//                 this.count++;
//                 this.$('.val').text(this.count);
//             }, 1000)
//         }
//     });
//     require('web.dom_ready')
//     var counter = new Counter(this, 4);
//
//     counter.appendTo("body");
//
// })