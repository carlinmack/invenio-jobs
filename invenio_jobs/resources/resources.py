# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 CERN.
#
# Invenio-Jobs is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Resources definitions."""

from flask import g
from flask_resources import Resource, resource_requestctx, response_handler, route
from invenio_records_resources.resources.errors import ErrorHandlersMixin
from invenio_records_resources.resources.records.resource import (
    request_data,
    request_headers,
    request_search_args,
    request_view_args,
)


class TasksResource(ErrorHandlersMixin, Resource):
    """Tasks resource."""

    def __init__(self, config, service):
        """Constructor."""
        super().__init__(config)
        self.service = service

    def create_url_rules(self):
        """Create the URL rules for the OAI-PMH server resource."""
        routes = self.config.routes
        url_rules = [
            route("GET", routes["list"], self.search),
        ]

        return url_rules

    #
    # Primary Interface
    #
    @request_search_args
    @response_handler(many=True)
    def search(self):
        """Perform a search."""
        identity = g.identity
        hits = self.service.search(
            identity=identity,
            params=resource_requestctx.args,
        )
        return hits.to_dict(), 200


class JobResource(ErrorHandlersMixin, Resource):
    """Jobs resource."""

    def __init__(self, config, service):
        """Constructor."""
        super().__init__(config)
        self.service = service

    def create_url_rules(self):
        """Create the URL rules for the OAI-PMH server resource."""
        routes = self.config.routes
        url_rules = [
            route("GET", routes["list"], self.search),
            route("POST", routes["list"], self.create),
            route("GET", routes["item"], self.read),
            route("PUT", routes["item"], self.update),
            route("DELETE", routes["item"], self.delete),
        ]

        return url_rules

    #
    # Primary Interface
    #
    @request_search_args
    @response_handler(many=True)
    def search(self):
        """Perform a search."""
        identity = g.identity
        hits = self.service.search(
            identity=identity,
            params=resource_requestctx.args,
        )
        return hits.to_dict(), 200

    @request_data
    @response_handler()
    def create(self):
        """Create an item."""
        item = self.service.create(
            g.identity,
            resource_requestctx.data or {},
        )
        return item.to_dict(), 201

    @request_view_args
    @response_handler()
    def read(self):
        """Read an item."""
        item = self.service.read(
            g.identity,
            resource_requestctx.view_args["id"],
        )
        return item.to_dict(), 200

    @request_headers
    @request_view_args
    @request_data
    @response_handler()
    def update(self):
        """Update an item."""
        item = self.service.update(
            g.identity,
            resource_requestctx.view_args["id"],
            resource_requestctx.data,
        )
        return item.to_dict(), 200

    @request_headers
    @request_view_args
    def delete(self):
        """Delete an item."""
        self.service.delete(
            g.identity,
            resource_requestctx.view_args["id"],
        )
        return "", 204


class RunsResource(ErrorHandlersMixin, Resource):
    """Runs resource."""

    def __init__(self, config, service):
        """Constructor."""
        super().__init__(config)
        self.service = service

    def create_url_rules(self):
        """Create the URL rules for the OAI-PMH server resource."""
        routes = self.config.routes
        url_rules = [
            route("GET", routes["list"], self.search),
            route("POST", routes["list"], self.create),
            route("GET", routes["item"], self.read),
            route("PUT", routes["item"], self.update),
            route("DELETE", routes["item"], self.delete),
        ]

        return url_rules

    #
    # Primary Interface
    #
    @request_search_args
    @response_handler(many=True)
    def search(self):
        """Perform a search."""
        identity = g.identity
        hits = self.service.search(
            identity=identity,
            params=resource_requestctx.args,
        )
        return hits.to_dict(), 200

    @request_data
    @response_handler()
    def create(self):
        """Create an item."""
        item = self.service.create(
            g.identity,
            resource_requestctx.data or {},
        )
        return item.to_dict(), 201

    @request_view_args
    @response_handler()
    def read(self):
        """Read an item."""
        item = self.service.read(
            g.identity,
            resource_requestctx.view_args["id"],
        )
        return item.to_dict(), 200

    @request_headers
    @request_view_args
    @request_data
    @response_handler()
    def update(self):
        """Update an item."""
        item = self.service.update(
            g.identity,
            resource_requestctx.view_args["id"],
            resource_requestctx.data,
        )
        return item.to_dict(), 200

    @request_headers
    @request_view_args
    def delete(self):
        """Delete an item."""
        self.service.delete(
            g.identity,
            resource_requestctx.view_args["id"],
        )
        return "", 204
