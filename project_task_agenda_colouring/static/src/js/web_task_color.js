odoo.define('project_task_agenda_colouring.web_task_color', function (require) {
    'use strict';

    var KanbanRecord = require('web.KanbanRecord');

    KanbanRecord.include({
        _render: function(){
            this._super.apply(this, arguments);
            if (this.modelName === 'project.task' && this.recordData.hex_value) {
                var $record = this.$el.css("background-color", this.recordData.hex_value || 'white');
            }
            else {
                this._super.apply(this, arguments);
            }
        }
    });

});