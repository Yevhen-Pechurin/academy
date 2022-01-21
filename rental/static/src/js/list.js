odoo.define('rental.list', function (require) {
    'use strict';

    var basicFields = require('web.basic_fields');
    var FieldChar = basicFields.FieldChar;
    var core = require('web.core');

    var QWeb = core.qweb;
    var fieldRegistry = require('web.field_registry');
    var jquery = require('web.jquery.extensions')


    const List = FieldChar.extend({
        events: _.extend({}, FieldChar.prototype.events, {
            'input': 'filterFunction',
        }),
        init: function () {
            const self = this;
            this._super.apply(this, arguments);
        },
        filterFunction: function () {
            const self = this;
            if (this.$el.val() == '') {
                self.$el.parent().find('.list_div').remove();
                return;
            }
            this._rpc({
                model: 'rental.car',
                method: 'get_cars',
                args: [this.$el.val()]
            }).then(res => {
                self.$el.parent().find('.list_div').remove();
                const elem = $(QWeb.render('rental.list', {
                    data: res,
                }));
                elem.find('.list_ul').on('click', self.setFunction.bind(self));
                $('#' + self.$el['0'].id).blur(function () {
                        self.$el.parent().find('.list_div').remove();
                        console.log(Math.random())
                    }
                )
                self.$el.after(elem);
            });
        },
        setFunction: function (params) {
            const self = this;
            this._rpc({
                model: 'rental.car',
                method: 'get_cars_info',
                args: [params.target.dataset.id]
            }).then(res => {
                self.$el.val(res[0].model);
                self.trigger_up('field_changed', {
                    dataPointID: self.dataPointID,
                    operation: 'UPDATE',
                    changes: {'model': res[0].model}
                });
                self.$el.parent().find('.list_div').remove();
            });
        }
        ,
    });
    fieldRegistry.add('list_widget', List);
})
