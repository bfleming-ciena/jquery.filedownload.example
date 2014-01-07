jquery.filedownload.example
===========================

Example of using jquery.filedownload with a python backend to download the file.


This plugin works by listening for a cookie named fileDownload=true.  That cookie is set by the URL that you pass to the plugin.

It is up to your server side code to send this cookie back. This informs the plugi to close it's dialog box.

If that fileDownload cookie is not cleared, say it is set to true, the plugin will open the dialog and close immediately.  Delete that cookie to fix that issue.

In short, this plugin doesn't from a UX point of view except displays a dialog when the download is occuring and makes the dialog go away when the download is done, toally based on that cookie being set.


