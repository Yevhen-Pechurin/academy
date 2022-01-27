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
            this.name = '';
            this._super.apply(this, arguments);
        },
        filterFunction: function () {
            this.name = this.$el['0']['name']
            const self = this;
            if (this.$el.val() == '') {
                self.$el.parent().find('.list_div').remove();
                return;
            }
            this._rpc({
                model: 'rental.car',
                method: 'get_cars',
                args: [this.$el.val(), this.name]
            }).then(res => {
                console.log(res);
                self.$el.parent().find('.list_div').remove();
                const elem = $(QWeb.render('rental.list', {
                    data: res,
                }));
                $(document).mouseup(function (e) {
                    var div = $(".list_div");
                    if (!div.is(e.target)
                        && div.has(e.target).length === 0) {
                        self.$el.parent().find('.list_div').remove();

                    }
                });
                elem.find('.list_div').on('click', self.setFunction.bind(self));

                self.$el.after(elem);
            });
        },
        setFunction: function (params) {
            const self = this;
            this._rpc({
                model: 'rental.car',
                method: 'get_cars_info',
                args: [params.target.dataset.id, this.name]
            }).then(res => {
                var dictionary = {}
                dictionary[this.name] = res[0][this.name]
                self.$el.val(res[0][this.name]);
                self.trigger_up('field_changed', {
                    dataPointID: self.dataPointID,
                    operation: 'UPDATE',
                    changes: dictionary
                });
                self.$el.parent().find('.list_div').remove();
            });
        },
    });
    fieldRegistry.add('list_widget', List);
})
