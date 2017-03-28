# G Suite

## Domain

### Multiple domains in one account

Primary domain  (e.g. example.com)
Separate domain (e.g. othercompany.com)

jan.code@example.com
feb.line@othercompany.com

1. You will only ever have one primary domain.

1. You can add up to 500 domains to your organisation's Google account including 20 domain aliases.

1. Adding a domain alias or customising web addresses can only be done with a primary domain.

1. You cannot set different policies, configuration settings or restrict sharing based on a domain.

### Domain Alias Limitations

Primary domain (e.g. example.com)
Domain alias (e.g. example.co.uk)

jan.code@example.com
jan.code@example.co.uk

1. Domain aliases can only be added to primary domain.

1. Limit of 20 Domain Aliases per G Suite Account.

1. Users must still sign in to their Google accounts using their primary domain address.

### Domain verification options 

1. Add a ATXT record or CNAME record to your domain's DNS settings at your domain host's website. (RECOMMENDED)
   (May take up to one hour after adding the record to reflect the change).


1. Upload an HTML file to your domain's web server if you don't have access yo uout domain's DNS settings.

1. Add a <meta> tag to your home page by editing a file on your domain's web server.

### Mail Exchange (MX) records

Control how incoming email is routed for your domain.
Before Google can host email you'll need to change these MX records to point to Google's Mail servers.

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

### To create or view an SPF record for your company's domain:

You must have access to your DNS registrar to create or view the DNS TXT record for SPF.

Sign in to your DNS registrar as the administrator user.

If you purchased your domain from Google, locate the TXT record configured for SPF.

If you didn't purchase your domain from Google, create a TXT record using the following information (note that the values for the DNS TXT record vary between DNS registrars; look for your registrar from the [list of specific DNS providers](https://support.google.com/a/topic/1409901)). Example for GoDaddy and many registrars:

```
Hostname: @
Record value: v=spf1 include:_spf.google.com ~all
```

Learn more about [DNS TXT records](https://support.google.com/a/answer/2716800).

Note: It may take up to 48 hours for DNS changes to fully propagate.

If you have multiple domains in your company, you must complete these steps for every domain.

### To configure DKIM for your company's domain

1. Sign in to your domain's G Suite Admin console as the G Suite super administrator.

1. Click the **G Suite** icon.

1. Select **Gmail** > **Authenticate email**.

1. Select your domain from the drop-down list.
If you have multiple domains in your company, you can select another domain name.

1. Click the **Generate new record** link.

1. Use Prefix selector **google**.
Note: You only need to change the prefix if you're already using **google** as another prefix.

1. Click **Generate**.
The Admin console displays the hostname and TXT record value you must configure with your DNS registrar.

1. Sign in to your DNS registrar and create a TXT record using the DNS hostname and record value provided by Google.
Note: The values for the [DNS TXT record](https://support.google.com/a/answer/2716800) vary between DNS registrars, so look for your registrar from the [list of specific DNS providers](https://support.google.com/a/topic/1409901).

1. When you're done creating the DNS TXT records, go back to your G Suite Admin console and click **Start authentication**.
If you don't want to configure DKIM, close the Authenticate email window.

Note: It can take up to 48 hours for DNS changes to fully propagate.

## Mobile Device Management

### To enforce Android device management

1. In the Admin console, “Manage Android Devices” security policy enforcement must be enabled.

1. On the device, the latest version of the G Suite Device Policy application must be installed.

### To remotely wipe the device

1. In the Admin console, Allow user to remote wipe device is enabled.

1. On the device, G Suite Device Policy is installed.

1. Use **Remote Wipe** to delete everything (including SD card and all personal data).
   Use **Wipe Account** to delete only G Suite data.
   See [Remove corporate data from a mobile device](https://support.google.com/a/answer/173390?hl=en)


### To reset the sign-in cookies for a user:

1. Sign in to your domain's G Suite Admin console as the administrator user using the firstname.lastname@yourdomain.com format.

1. Click the Users icon.

1. From the user list, click the username.
Once the page has loaded, click Account, which displays the user's profile.
In the Password section, click Reset sign-in cookies.

1. Click Reset sign-in cookies.

It can take up to 60 minutes to sign out the user from current Gmail HTTP sessions. The logout time for other applications can vary.

## Security

1. To require users to sign in to G Suite using their LDAP credentials, Single Sign On should be enabled in your domain.

1. Google's 2-Step Verification cannot be ussed for accounts using a SAML single sign-on service.
   But you can get a 3rd party SSO solution that has 2-Step Verification included.

### Admin Account Recovery

1. Accounts with 3 super administrators or 500+ users, the email and phone methods **are not** available.

