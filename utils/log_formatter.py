from flask import has_request_context, request
import logging

class LogFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url          = request.url
            record.remoteaddr   = request.remote_addr
        else:
            record.url          = "[Non-Request]"
            record.remoteaddr   = "Local"

        return super().format(record)