# Veeva Vault SDK - API Implementation Checklist

This checklist outlines the features to be implemented in the Veeva Vault SDK. It is based on the auto-generated API client and the official Veeva Vault API documentation.

**Legend:**
*   `[x]` - Already implemented in `VaultClient`
*   `[ ]` - Not yet implemented

### Authentication

*   `[x]` Authenticate with username and password
*   `[x]` Authentication Type Discovery
*   `[ ]` OAuth 2.0 / OpenID Connect
*   `[ ]` Session Keep Alive
*   `[ ]` End Session
*   `[ ]` Initiate Delegated Session
*   `[ ]` Retrieve Delegations

### VQL (Vault Query Language)

*   `[x]` Submit a Query
*   `[ ]` Next Page URL
*   `[ ]` Previous Page URL

### Document Management

*   `[x]` Create Single Document
*   `[x]` Retrieve Document
*   `[x]` Update Single Document
*   `[ ]` Delete Single Document
*   `[ ]` Create Multiple Documents
*   `[ ]` Update Multiple Documents
*   `[ ]` Delete Multiple Documents
*   `[ ]` Create Single Document Version
*   `[ ]` Create Multiple Document Versions
*   `[ ]` Retrieve Document Versions
*   `[ ]` Retrieve Document Version
*   `[ ]` Update Document Version
*   `[ ]` Delete Single Document Version
*   `[ ]` Delete Multiple Document Versions
*   `[ ]` Download Document File
*   `[ ]` Download Document Version File
*   `[ ]` Download Document Thumbnail File
*   `[ ]` Download Document Version Thumbnail File
*   `[ ]` Add Single Document Rendition
*   `[ ]` Add Multiple Document Renditions
*   `[ ]` Retrieve Document Renditions
*   `[ ]` Replace Document Rendition
*   `[ ]` Delete Single Document Rendition
*   `[ ]` Delete Multiple Document Renditions
*   `[ ]` Download Document Rendition File
*   `[ ]` Download Document Version Rendition File
*   `[ ]` Create Document Attachment
*   `[ ]` Create Multiple Document Attachments
*   `[ ]` Retrieve Document Attachments
*   `[ ]` Retrieve Document Version Attachments
*   `[ ]` Update Document Attachment Description
*   `[ ]` Update Multiple Document Attachment Descriptions
*   `[ ]` Delete Single Document Attachment
*   `[ ]` Delete Multiple Document Attachments
*   `[ ]` Download Document Attachment
*   `[ ]` Download All Document Attachments
*   `[ ]` Download Document Attachment Version
*   `[ ]` Download All Document Version Attachments
*   `[ ]` Restore Document Attachment Version
*   `[ ]` Delete Single Document Attachment Version
*   `[ ]` Create Single Document Relationship
*   `[ ]` Create Multiple Document Relationships
*   `[ ]` Retrieve Document Relationships
*   `[ ]` Delete Single Document Relationship
*   `[ ]` Delete Multiple Document Relationships
*   `[ ]` Retrieve Document Roles
*   `[ ]` Retrieve All Document Roles
*   `[ ]` Assign Users & Groups to Roles on a Single Document
*   `[ ]` Assign Users & Groups to Roles on Multiple Documents & Binders
*   `[ ]` Remove Users & Groups from Roles on a Single Document
*   `[ ]` Remove Users and Groups from Roles on Multiple Documents & Binders
*   `[ ]` Retrieve Document User Actions
*   `[ ]` Retrieve User Actions on Multiple Documents
*   `[ ]` Initiate Document User Action
*   `[ ]` Initiate Bulk Document User Actions
*   `[ ]` Retrieve Document Entry Criteria
*   `[ ]` Reclassify Multiple Documents
*   `[ ]` Export Documents
*   `[ ]` Retrieve Document Export Results
*   `[ ]` Export Document Versions
*   `[ ]` Retrieve Deleted Document IDs
*   `[ ]` Retrieve Complete Audit History for a Single Document
*   `[ ]` Read Annotations by Document Version and Type
*   `[ ]` Read Annotations by ID
*   `[ ]` Read Replies of Parent Annotation
*   `[ ]` Create Multiple Annotations
*   `[ ]` Update Annotations
*   `[ ]` Delete Annotations
*   `[ ]` Add Annotation Replies
*   `[ ]` Export Document Annotations to PDF
*   `[ ]` Import Document Annotations from PDF
*   `[ ]` Retrieve Document Version Notes as CSV
*   `[ ]` Retrieve Anchor IDs
*   `[ ]` Create Document Lock
*   `[ ]` Retrieve Document Lock
*   `[ ]` Delete Document Lock
*   `[ ]` Undo Collaborative Authoring Checkout
*   `[ ]` Document Tokens
*   `[ ]` Create Document Template
*   `[ ]` Retrieve Document Template Collection
*   `[ ]` Retrieve Document Template Attributes
*   `[ ]` Update Single Document Template
*   `[ ]` Update Multiple Document Templates
*   `[ ]` Delete Basic Document Template
*   `[ ]` Download Document Template File

### Binder Management

*   `[ ]` Create Binder
*   `[ ]` Retrieve Binder
*   `[ ]` Update Binder
*   `[ ]` Delete Binder
*   `[ ]` Create Binder Version
*   `[ ]` Retrieve All Binder Versions
*   `[ ]` Retrieve Binder Version
*   `[ ]` Update Binder Version
*   `[ ]` Delete Binder Version
*   `[ ]` Add Document to Binder
*   `[ ]` Remove Document from Binder
*   `[ ]` Move Document in Binder
*   `[ ]` Create Binder Section
*   `[ ]` Update Binder Section
*   `[ ]` Delete Binder Section
*   `[ ]` Retrieve Binder Sections
*   `[ ]` Retrieve Binder Version Section
*   `[ ]` Update Binding Rule
*   `[ ]` Update Binder Document Binding Rule
*   `[ ]` Update Binder Section Binding Rule
*   `[ ]` Refresh Binder Auto-Filing
*   `[ ]` Export Binder (Latest Version)
*   `[ ]` Export Binder (Specific Version)
*   `[ ]` Retrieve Binder Export Results
*   `[ ]` Create Binder Template
*   `[ ]` Retrieve Binder Template Collection
*   `[ ]` Retrieve Binder Template Metadata
*   `[ ]` Update Binder Template
*   `[ ]` Delete Binder Template
*   `[ ]` Create Binder Template Node
*   `[ ]` Retrieve Binder Template Node Attributes
*   `[ ]` Replace Binder Template Nodes
*   `[ ]` Retrieve Binder Template Node Metadata

### Object Management

*   `[ ]` Create & Upsert Object Records
*   `[ ]` Retrieve Object Record
*   `[ ]` Update Object Records
*   `[ ]` Delete Object Records
*   `[ ]` Retrieve Object Record User Actions
*   `[ ]` Retrieve Object User Actions Details
*   `[ ]` Initiate Object Action on a Single Record
*   `[ ]` Initiate Object Action on Multiple Records
*   `[ ]` Change Object Type
*   `[ ]` Deep Copy Object Record
*   `[ ]` Retrieve Results of Deep Copy Job
*   `[ ]` Cascade Delete Object Record
*   `[ ]` Retrieve Results of Cascade Delete Job
*   `[ ]` Initiate Record Merge
*   `[ ]` Retrieve Record Merge Status
*   `[ ]` Retrieve Record Merge Results
*   `[ ]` Download Merge Records Job Log
*   `[ ]` Retrieve Object Record Roles
*   `[ ]` Create Object Record Attachment
*   `[ ]` Create Multiple Object Record Attachments
*   `[ ]` Retrieve Object Record Attachments
*   `[ ]` Retrieve Object Record Attachment Metadata
*   `[ ]` Update Object Record Attachment Description
*   `[ ]` Update Multiple Object Record Attachment Descriptions
*   `[ ]` Delete Object Record Attachment
*   `[ ]` Delete Multiple Object Record Attachments
*   `[ ]` Download All Object Record Attachment Files
*   `[ ]` Retrieve Object Record Attachment Versions
*   `[ ]` Retrieve Object Record Attachment Version Metadata
*   `[ ]` Restore Object Record Attachment Version
*   `[ ]` Delete Object Record Attachment Version
*   `[ ]` Download Object Record Attachment File
*   `[ ]` Update Attachment Field File
*   `[ ]` Download Attachment Field File
*   `[ ]` Download All Attachment Field Files
*   `[ ]` Recalculate Roll-up Fields
*   `[ ]` Retrieve Roll-up Field Recalculation Status
*   `[ ]` Update Corporate Currency Fields

### Workflow Management

*   `[ ]` Retrieve All Document Workflows
*   `[ ]` Retrieve Document Workflow Details
*   `[ ]` Initiate Document Workflow
*   `[ ]` Retrieve All Multi-Record Workflows
*   `[ ]` Retrieve Multi-Record Workflow Details
*   `[ ]` Initiate Multi-Record Workflow
*   `[ ]` Retrieve Workflows
*   `[ ]` Retrieve Workflow Details
*   `[ ]` Retrieve Workflow Actions
*   `[ ]` Retrieve Workflow Action Details
*   `[ ]` Initiate Workflow Action
*   `[ ]` Retrieve Workflow Tasks
*   `[ ]` Retrieve Workflow Task Details
*   `[ ]` Retrieve Workflow Task Actions
*   `[ ]` Retrieve Workflow Task Action Details
*   `[ ]` Accept Single Record Workflow Task
*   `[ ]` Complete Single Record Workflow Task
*   `[ ]` Reassign Single Record Workflow Task
*   `[ ]` Accept Multi-item Workflow Task
*   `[ ]` Complete Multi-item Workflow Task
*   `[ ]` Reassign Multi-item Workflow Task
*   `[ ]` Manage Multi-Item Workflow Content
*   `[ ]` Cancel Workflow Tasks
*   `[ ]` Cancel Workflows
*   `[ ]` Undo Workflow Task Acceptance
*   `[ ]` Update Workflow Task Due Date

### Audit Trail

*   `[ ]` Retrieve Audit Types
*   `[ ]` Retrieve Audit Metadata
*   `[ ]` Retrieve Audit Details
*   `[ ]` Retrieve Complete Audit History for a Single Object Record

### MDL (Metadata Definition Language)

*   `[ ]` Retrieve Component Record (MDL)
*   `[ ]-` Retrieve Content File
*   `[ ]` Upload Content File
*   `[ ]` Execute MDL Script
*   `[ ]` Execute MDL Script Asynchronously
*   `[ ]` Retrieve Asynchronous MDL Script Results

### Vault UI Code

*   `[ ]` Add or Replace Single Source Code File
*   `[ ]` Retrieve Single Source Code File
*   `[ ]` Delete Single Source Code File
*   `[ ]` Enable Vault Extension
*   `[ ]` Disable Vault Extension
*   `[ ]` Create Profiling Session
*   `[ ]` Retrieve All Profiling Sessions
*   `[ ]` Retrieve Profiling Session
*   `[ ]` Delete Profiling Session
*   `[ ]` End Profiling Session
*   `[ ]` Download Profiling Session Results
*   `[ ]` Add or Replace Single Client Code Distribution
*   `[ ]` Retrieve All Client Code Distribution Metadata
*   `[ ]` Retrieve Single Client Code Distribution Metadata
*   `[ ]` Delete Single Client Code Distribution
*   `[ ]` Download Single Client Code Distribution

### SCIM (System for Cross-domain Identity Management)

*   `[ ]` Retrieve All Users with SCIM
*   `[ ]` Retrieve Single User with SCIM
*   `[ ]` Create User with SCIM
*   `[ ]` Update User with SCIM
*   `[ ]` Retrieve Current User with SCIM
*   `[ ]` Update Current User with SCIM
*   `[ ]` Retrieve All SCIM Resource Types
*   `[ ]` Retrieve Single SCIM Resource Type
*   `[ ]` Retrieve All SCIM Schema Information
*   `[ ]` Retrieve Single SCIM Schema Information
*   `[ ]` Retrieve SCIM Provider

### Miscellaneous

*   `[ ]` Retrieve Limits on Objects
*   `[ ]` Download Daily API Usage
*   `[ ]` Retrieve All Picklists
*   `[ ]` Retrieve Picklist Values
*   `[ ]` Create Picklist Values
*   `[ ]` Update Picklist Value
*   `[ ]` Update Picklist Value Label
*   `[ ]` Inactivate Picklist Value
*   `[ ]` Retrieve All Groups
*   `[ ]` Retrieve Group
*   `[ ]` Create Group
*   `[ ]` Update Group
*   `[ ]` Delete Group
*   `[ ]` Retrieve Auto Managed Groups
*   `[ ]` Retrieve All Security Policies
*   `[ ]` Retrieve Security Policy
*   `[ ]` Retrieve All Users
*   `[ ]` Retrieve User
*   `[ ]` Create Single User
*   `[ ]` Update Single User
*   `[ ]` Update Multiple Users
*   `[ ]` Disable User
*   `[ ]` Validate Session User
*   `[ ]` Change My Password
*   `[ ]` Retrieve User Permissions
*   `[ ]` Retrieve My User Permissions
*   `[ ]` Update Vault Membership
*   `[ ]` Retrieve Application License Usage
*   `[ ]` Retrieve Domain Information
*   `[ ]` Retrieve Domains
*   `[ ]` Retrieve Sandboxes
*   `[ ]` Retrieve Sandbox Details by ID
*   `[ ]` Create or Refresh Sandbox
*   `[ ]` Delete Sandbox
*   `[ ]` Change Sandbox Size
*   `[ ]` Build Production Vault
*   `[ ]` Promote to Production
*   `[ ]` Recheck Sandbox Usage Limit
*   `[ ]` Create Sandbox Snapshot
*   `[ ]` Retrieve Sandbox Snapshots
*   `[ ]` Update Sandbox Snapshot
*   `[ ]` Upgrade Sandbox Snapshot
*   `[ ]` Delete Sandbox Snapshot
*   `[ ]` Refresh Sandbox from Snapshot
*   `[ ]` Set Sandbox Entitlements
*   `[ ]` Add EDL Matched Documents
*   `[ ]` Remove EDL Matched Documents
*   `[ ]` Create a Placeholder from an EDL Item
*   `[ ]` Retrieve a Node's Children
*   `[ ]` Update Node Order
*   `[ ]` Retrieve Specific Root Nodes
*   `[ ]` Retrieve All Root Nodes
*   `[ ]` Retrieve Component Record (XML/JSON)
*   `[ ]` Retrieve Component Record Collection
*   `[ ]` Retrieve Details from a Specific Object
*   `[ ]` Retrieve Details from All Object Types
*   `[ ]` Retrieve Component Type Metadata
*   `[ ]` Retrieve All Component Metadata
*   `[ ]` Retrieve Document Type
*   `[ ]` Retrieve All Document Types
*   `[ ]` Retrieve Document Subtype
*   `[ ]` Retrieve Document Classification
*   `[ ]` Retrieve Document Type Relationships
*   `[ ]` Retrieve Document Event Types and Subtypes
*   `[ ]` Retrieve Document Event SubType Metadata
*   `[ ]` Retrieve Document Lock Metadata
*   `[ ]` Retrieve Common Document Fields
*   `[ ]` Retrieve All Document Fields
*   `[ ]` Retrieve Document Template Metadata
*   `[ ]` Retrieve Binder Template Node Metadata
*   `[ ]` Retrieve Group Metadata
*   `[ ]` Retrieve Security Policy Metadata
*   `[ ]` Retrieve User Metadata
*   `[ ]` Retrieve Archived Document Signature Metadata
*   `[ ]` Retrieve Document Signature Metadata
*   `[ ]` Retrieve Object Collection
*   `[ ]` Retrieve Object Metadata
*   `[ ]` Retrieve Object Field Metadata
*   `[ ]` Retrieve Page Layouts
*   `[ ]` Retrieve Page Layout Metadata
*   `[ ]` Retrieve Email Notification Histories
*   `[ ]` Retrieve Job Histories
*   `[ ]` Retrieve Job Monitors
*   `[ ]` Retrieve Job Status
*   `[ ]` Retrieve SDK Job Tasks
*   `[ ]` Retrieve Import Bulk Translation File Job Summary
*   `[ ]` Retrieve Import Bulk Translation File Job Errors
*   `[ ]` Retrieve Loader Extract Results
*   `[ ]` Retrieve Load Failure Log Results
*   `[ ]` Retrieve Load Success Log Results
*   `[ ]` Retrieve Loader Extract Renditions Results
*   `[ ]` Retrieve Outbound Package Dependencies
*   `[ ]` Retrieve Package Deploy Results
*   `[ ]` Retrieve Signing Certificate
*   `[ ]` Enable Configuration Mode
*   `[ ]` Disable Configuration Mode
*   `[ ]` List Items at a Path
*   `[ ]` Create Folder or File
*   `[ ]` Update Folder or File
*   `[ ]` Delete File or Folder
*   `[ ]` Download Item Content
*   `[ ]` Create Resumable Upload Session
*   `[ ]` Get Upload Session Details
*   `[ ]` Abort Upload Session
*   `[ ]` List File Parts Uploaded to Session
*   `[ ]` Commit Upload Session
*   `[ ]` Upload to a Session
*   `[ ]` Export Package
*   `[ ]` Import Package
*   `[ ]` Validate Package
*   `[ ]` Validate Imported Package
*   `[ ]` Vault Compare
*   `[ ]` Vault Configuration Report
*   `[ ]` Extract Data Files
*   `[ ]` Load Data Objects
*   `[ ]` Start Job
*   `[ ]` Retrieve All Queues
*   `[ ]` Retrieve Queue Status
*   `[ ]` Enable Delivery
*   `[ ]` Disable Delivery
*   `[ ]` Reset Queue
*   `[ ]` Component Definition Query
*   `[ ]` Cancel Raw Object Deployment
