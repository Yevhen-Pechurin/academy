odoo.define('rental_car.my_widget', function (require) {
    "use strict";

    var basicFields = require('web.basic_fields');
    var field_registry = require('web.field_registry');
    var FieldChar = basicFields.FieldChar
    var core = require('web.core');
    var QWeb = core.qweb;


        var MyWidget = FieldChar.extend({

        events: _.extend({}, FieldChar.prototype.events, {
            'input': '_onInput',
            // 'focusout': '_onFocusOut',
        }),
        init: function (){
            this._super.apply(this, arguments);

        },
        _onInput(){
            var self = this;
            var query = this.$el.val()
            this._rpc({
                model: 'rental_car.car',
                method: 'brand_list',
                args: [query],
            }).then((data) => {
                // console.log(data)
                if (data && data.length >= 0) {
                    var elem = $(QWeb.render('rental_car.brand_list', {
                        list_brand: data,


                    }));


                    elem.find('.list').on('click', this._onClickBrand.bind(this));
                    self.$el.after(elem);
                }
            })
        },
        _onClickBrand: function (e) {

            const self = this;
            this._rpc({
                model: 'rental_car.car',
                method: 'brand_info',
                args: [e.target.dataset.id]
            }).then((data) => {


                self.trigger_up('field_changed', {
                    dataPointID: self.dataPointID,
                    operation: 'UPDATE',
                    changes: {'number': data[0].name}
                });
                self.$el.parent().find('.brand_list').remove()
            });
        },
        // _onFocusOut(){
        //     this.$el.parent().find('.brand_list').remove()
        // }

    })

    field_registry.add('my_widget', MyWidget);
    return MyWidget;

});
