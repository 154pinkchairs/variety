# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (c) 2012, Peter Levi <peterlevi@peterlevi.com>
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE

import logging
import random
import requests

from variety.plugins.builtin.downloaders.LibredditDownloader import LibredditDownloader
from variety.plugins.downloaders.ConfigurableImageSource import ConfigurableImageSource
from variety.Util import _

random.seed()


logger = logging.getLogger("variety")


class LibredditSource(ConfigurableImageSource):
    @classmethod
    def get_info(cls):
        return {
            "name": "LibredditSource",
            "description": _("Configurable source for fetching images from Libreddit (a privacy-friendly, decentralized Reddit frontend)"),
            "author": "Marcelina Hołub",
            "version": "0.1",
        }

    def get_source_type(self):
        return "libreddit"

    def get_source_name(self):
        return "Libreddit"

    def get_ui_instruction(self):
        return _(
            "Enter the name of a subreddit or paste the full URL of a subreddit or a "
            "<a href='http://reddit.com'>Reddit</a> user. You may specify sort order and time "
            "period if you wish. Variety will use posts to direct images or to Imgur pages "
            "within the first 100 submissions returned by the chosen Libreddit instance.\n\n"
            "Example: You may specify simply 'comics' or "
            "<a href='http://libredd.it/r/comics'>http://libredd.it/r/comics</a>\n"
            "Example: Top posts from the month: "
            "<a href='https://libreddit.spike.codes/r/comics/top?t=month'>https://libreddit.spike.codes/r/comics/top?t=month</a>"
        )
    #def instance(instances):
        #instances = ["https://libreddit.spike.codes", "https://libredd.it", "https://libreddit.dothq.co", "https://libreddit.kavin.rocks", "https://reddit.invak.id", "https://lr.riverside.rocks", "https://libreddit.strongthany.cc", "https://libreddit.privacy.com.de", "https://reddit.artemislena.eu", "https://libreddit.some-things.org", "https://reddit.stuehieyr.com", "https://lr.mint.lgbt", "https://libreddit.igna.rocks", "https://lr.oversold.host", "https://libreddit.de", "https://libreddit.pussthecat.org", "https://leddit.xyz", "https://libreddit.nl", "https://libreddit.bus-hit.me"]
        #return
    def instance_button(self):
        return _("Libreddit instance:")
    def on_instance_button_clicked():
        instances = ["https://libreddit.spike.codes", "https://libredd.it", "https://libreddit.dothq.co", "https://libreddit.kavin.rocks", "https://reddit.invak.id", "https://lr.riverside.rocks", "https://libreddit.strongthany.cc", "https://libreddit.privacy.com.de", "https://reddit.artemislena.eu", "https://libreddit.some-things.org", "https://reddit.stuehieyr.com", "https://lr.mint.lgbt", "https://libreddit.igna.rocks", "https://lr.oversold.host", "https://libreddit.de", "https://libreddit.pussthecat.org", "https://leddit.xyz", "https://libreddit.nl", "https://libreddit.bus-hit.me"]
        combobox = gtk.ComboBox()
        store = gtk.ListStore(gobject.TYPE_STRING)
        cell = gtk.CellRendererText()
        combobox.pack_start(cell)
        for i in instances and n in range(len(instances)):
            combobox.add_attribute(cell, i, n)
    def get_ui_short_instruction(self):
        return _("URL or name of a subreddit: ")

    def get_ui_short_description(self):
        return _("Fetch images from a given subreddit or user")

    def validate(self, instance, query):
        logger.info(lambda: f"Validating Libreddit query {query}")
        if "/" not in query:
            query = "%s/r/%s" % instance, query
        try:
            if not instance.startswith("http://") and not instance.startswith("https://"):
                query = f"https://{query}"
            isValid = [url for url in instances if(url in query)]
            if not bool(isValid):
                return False, _("This does not seem to be a valid Libreddit instance URL")

            dl = LibredditDownloader(self, query)
            queue = dl.fill_queue()
            return (
                query,
                None if len(queue) > 0 else _("We could not find any image submissions there."),
            )
        except Exception:
            logger.exception(
                lambda: "Error while validating URL, probably no image posts for this URL"
            )
            return query, _("We could not find any image submissions there.")

    def create_downloader(self, config):
        return LibredditDownloader(self, config)
