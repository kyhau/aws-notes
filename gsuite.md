# G Suite

## Drive

1. Drive stores at most 4,000 items or 5GB of data offline.

1. You can restore a given user's deleted Google Drive files for a date range you specify, as long as the Drive files were deleted within the past 25 days.

1. If a user provides others with access to any Drive item, when you restore that item, the access is not restored. The user can re-enable access as needed.

1. By default, each user with a G Suite account has 30 GB of storage available for uploaded Google Drive files, Gmail, and Google+ photos. Users with the free edition of G Suite (or consumer accounts) get 15 GB of storage.

## Gmail

### Prevent Spammers from Forging Your Domain

Google supports several methods of preventing spammers from forging users in your domain.

1. [Sender Policy Framework (SPF) records](https://support.google.com/a/answer/33786)
1. [DomainKeys Identified Mail (DKIM)](https://support.google.com/a/answer/174124)
1. (NEWER method) [Domain-based Message Authentication, Reporting & Conformance (DMARC)](https://support.google.com/a/answer/2466580)

You must create DNS TXT records to configure these email security features and allow access to your DNS registrar, such as GoDaddy or eNom. Learn more about [Domain Name Service (DNS) basics](https://support.google.com/a/answer/48090).

Note: If you purchased your domain from Google, the SPF record is already created. Also your DNS registrar credentials are available in your G Suite Admin console.
