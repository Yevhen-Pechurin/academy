odoo.define('rental_car.widget', function (require) {
    'use strict';

    const FieldChar = require("web.basic_fields").FieldChar;
    const fieldRegistry = require('web.field_registry');
    const CustomFieldChar = FieldChar.extend({
       events: _.extend({},FieldChar.prototype.events,{
           'input': "_onInput",
       }),
        init: function (){
           this._super.apply(this, arguments)
           console.log("CustomField>>>>>init")
       },
        _onInput:function () {
          console.log(this.$el.val());
        },

    });
    // fieldRegistry.add('my-custom-field', CustomFieldChar);
    fieldRegistry.add('my_custom_widget', CustomFieldChar)
});