// This file is part of Invenio
// Copyright (C) 2024 CERN.
//
// Invenio RDM is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.

import { initDefaultSearchComponents } from "@js/invenio_administration";
import { createSearchAppInit } from "@js/invenio_search_ui";
import { NotificationController } from "@js/invenio_administration";
import { SearchResultItemLayout } from "./RunsSearchResultItemLayout";
import { JobSearchLayout } from "./JobSearchLayout";
import { JobRunsTitle } from "./JobRunsTitle";

const domContainer = document.getElementById("invenio-search-config");

const defaultComponents = initDefaultSearchComponents(domContainer);

const overridenComponents = {
  ...defaultComponents,
  "InvenioAdministration.SearchResultItem.layout": SearchResultItemLayout,
  "SearchApp.layout": JobSearchLayout,
};

createSearchAppInit(
  overridenComponents,
  true,
  "invenio-search-config",
  false,
  NotificationController
);

const pidValue = domContainer.dataset.pidValue;

JobRunsTitle(pidValue);