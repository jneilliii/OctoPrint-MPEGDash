/*
 * View model for MPEG-Dash
 *
 * Author: jneilliii
 * License: AGPLv3
 */
$(function() {
    function Mpeg_dashViewModel(parameters) {
        var self = this;

        self.settingsViewModel = parameters[0];

        // TODO: Implement your plugin's view model here.
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: Mpeg_dashViewModel,
        dependencies: ["settingsViewModel"],
        elements: ["#tab_plugin_mpeg_dash"]
    });
});
