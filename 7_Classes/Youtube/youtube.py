#!/usr/bin/env python3

import re
import urllib

web_obj = urllib.urlopen("http://gdata.youtube.com/feeds/api/standardfeeds/top_rated?maxresults=5&time=today")
results_str = web_obj.read()
web_obj.close()

class Query(object):
    """ The Query class will perform the actual HTTP request and initial parsing to build the Video objects
        from the response. It will also calculate the following information based on the video and user results.
    """

    def __init__(self, feed_id, max_result):
        """ Takes as input the type of query (feed_id)
            and the maximum number of results (max_results) that the query should obtain.
            Results are converted into Video objects, which are stored within this class.
        """
        self.__video = Video

    def __str__(self):
        """ Use print() function to show information on each video and YouTube user, including the
            aforementioned statistics data. """


class User(object):
    """ The User class will perform another query to obtain detailed information about the uploader of a video.
        This class stores: name, subscriberCount, totalUploadViews.
    """

    def __init__(self, author_str):
    """ author_str is parsed to extract YouTube username of the Video’s uploader (name).
        HTTP request is constructed and submitted to obtain the extra information (subscriberCount, totalUploadViews) about the uploader.
    """

    def __str__(self):
    """ Make print() function to display information about the user.
    """

class Video(object):
    """ The Video class tracks information about a single YouTube video, including:
        media:title, user(User class), media:description, favoriteCount, viewCount.
    """

    def __init__(self, entry_str):
        """ 'entry_str' is parsed to extract the various pieces of information
             and the text to create the User instance.
        """

    def __str__(self):
        """ Make print() function to display the stored Video data, as well as data for the
            associated uploader.
        """

