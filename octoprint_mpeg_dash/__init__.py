# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class Mpeg_dashPlugin(octoprint.plugin.SettingsPlugin,
                      octoprint.plugin.AssetPlugin,
                      octoprint.plugin.TemplatePlugin):

	##~~ SettingsPlugin mixin

	def get_settings_defaults(self):
		return dict(
			url=""
		)

	##~~ AssetPlugin mixin

	def get_assets(self):
		# Define your plugin's asset files to automatically include in the
		# core UI here.
		return dict(
			js=["js/mpeg_dash.js","js/dash.all.min.js"],
			css=["css/mpeg_dash.css"]
		)

	##~~ Softwareupdate hook

	def get_update_information(self):
		# Define the configuration for your plugin to use with the Software Update
		# Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
		# for details.
		return dict(
			mpeg_dash=dict(
				displayName="MPEG-Dash",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="jneilliii",
				repo="OctoPrint-MPEGDash",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/jneilliii/OctoPrint-MPEGDash/archive/{target_version}.zip"
			)
		)

__plugin_name__ = "MPEG-Dash"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = Mpeg_dashPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

