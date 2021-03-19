# Statuspage-automation
Posting a statuspage via API's

Statuspage is the communication piece of your incident management process. It will easily communicate real-time status to your users. 

API keys are managed by account owners at the organization level. Team members can view the organization and page IDs needed when using the API, but not API keys.

Incidents are the best way to communicate with your customers during downtime. 

This workflow is to create incident on the statuspage via jenkins pipeline using the string parameter. 

jenkins pipeline string parameters are : "Incident", "Infrastructure" and "Email"

NOTE: Each of your status pages has a unique ID that you’ll refer to when using the API. eg: page ID: sdfkjhsphjs3epy

Each incident/component has unique ID that you will refer to when using the API.

Component statuses: “operational", "under_maintenance", "degraded_performance", "partial_outage" and "major_outage"
