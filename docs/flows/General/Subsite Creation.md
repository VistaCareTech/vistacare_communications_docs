# Sharepoint Subsite Creation - Setting Up New Xplore Areas

When a new area is created within the Xplore project, it is necessary to create a new subsite for this new area within the Xplore subsite.

Below is a step-by-step guide on how to do this.

1. Once inside the <a href="https://vistacaretech.sharepoint.com/sites/engineering/xplore/_layouts/15/viewlsts.aspx?view=15" target="_blank">Xplore subsite</a>, click on the **Site Contents**. Then click on **New** and on **Subsite**. You will be redirected to a new page.

<a class="" data-lightbox="Sharepoint Subsite Creation - Step 1" href="../../../_static/flows/map_sharepoint/map_sharepoint_-_step_1.png" title="Sharepoint Subsite Creation - Step 1" data-title="Sharepoint Subsite Creation - Step 1"><img src="../../../_static/flows/map_sharepoint/map_sharepoint_-_step_1.png" class="align-center" width="800px" height="500px" alt="Sharepoint Subsite Creation - Step 1">
</a>

2. On this new page, the following fields need to be filled in:

* **Title field**: type the name of the area followed by the Job Number.

* **Description field**: type Xplore followed by the area name and the Job Number.

* **URL name**: type the Job Number.

* **Template Selection**: Select the option **Team site (no Microsoft 365 group)**.

* **Permissions**: Select the option **Use same permissions as parent site**.

* **Navigation Inheritance**: Under **Use the top link bar from the parent site?**, select **Yes**.

After filling in the fields, click on the **Create** button. Once this is done, you will be redirected to the newly created subsite.

<a class="" data-lightbox="Sharepoint Subsite Creation - Step 2" href="../../../_static/flows/map_sharepoint/map_sharepoint_-_step_2.png" title="Sharepoint Subsite Creation - Step 2" data-title="Sharepoint Subsite Creation - Step 2"><img src="../../../_static/flows/map_sharepoint/map_sharepoint_-_step_2.png" class="align-center" width="800px" height="500px" alt="Sharepoint Subsite Creation - Step 2">
</a>

3. Within the new subsite, click on the **Site Contents** and then on **Return to classic SharePoint** in the bottom left corner of the screen. This is necessary so that we can create new lists using the pre-made templates.

<a class="" data-lightbox="Sharepoint Subsite Creation - Step 3" href="../../../_static/flows/map_sharepoint/map_sharepoint_-_step_3.png" title="Sharepoint Subsite Creation - Step 3" data-title="Sharepoint Subsite Creation - Step 3"><img src="../../../_static/flows/map_sharepoint/map_sharepoint_-_step_3.png" class="align-center" width="800px" height="500px" alt="Sharepoint Subsite Creation - Step 3">
</a>

4. Click on **add an app**, and then in the search bar type **Job List**. An app/list called Job List should be found. Click on it, and in the window that opens type Job List as the name.

<a class="" data-lightbox="Sharepoint Subsite Creation - Step 4" href="../../../_static/flows/map_sharepoint/map_sharepoint_-_step_4.png" title="Sharepoint Subsite Creation - Step 4" data-title="Sharepoint Subsite Creation - Step 4"><img src="../../../_static/flows/map_sharepoint/map_sharepoint_-_step_4.png" class="align-center" width="800px" height="500px" alt="Sharepoint Subsite Creation - Step 4">
</a>

5. Click on **add an app** again, and then in the search bar type **Task List**. An app/list called Task List should be found. Click on it, and in the window that opens type Task List as the name.

<a class="" data-lightbox="Sharepoint Subsite Creation - Step 5" href="../../../_static/flows/map_sharepoint/map_sharepoint_-_step_5.png" title="Sharepoint Subsite Creation - Step 5" data-title="Sharepoint Subsite Creation - Step 5"><img src="../../../_static/flows/map_sharepoint/map_sharepoint_-_step_5.png" class="align-center" width="800px" height="500px" alt="Sharepoint Subsite Creation - Step 5">
</a>

6. Click on **add an app** again, and then in the search bar type **Task Capacities**. An app/list called **Task Capacities Xplore** should be found. Click on it, and in the window that opens, type Task Capacities as the name.

<a class="" data-lightbox="Sharepoint Subsite Creation - Step 6" href="../../../_static/flows/map_sharepoint/map_sharepoint_-_step_6.png" title="Sharepoint Subsite Creation - Step 6" data-title="Sharepoint Subsite Creation - Step 6"><img src="../../../_static/flows/map_sharepoint/map_sharepoint_-_step_6.png" class="align-center" width="800px" height="500px" alt="Sharepoint Subsite Creation - Step 6">
</a>

7. Once you have created the **Task Capacities** list, click to access it. Then click on the **Subsequent Tasks** column > **Column Settings** > **Edit**. In **Select a list as a source** select Task Capacities. And in **Select a column from the list above** select the Task column. Click Save.

<a class="" data-lightbox="Sharepoint Subsite Creation - Step 7" href="../../../_static/flows/map_sharepoint/map_sharepoint_-_step_7.png" title="Sharepoint Subsite Creation - Step 7" data-title="Sharepoint Subsite Creation - Step 7"><img src="../../../_static/flows/map_sharepoint/map_sharepoint_-_step_7.png" class="align-center" width="800px" height="500px" alt="Sharepoint Subsite Creation - Step 7">
</a>

8. Again click on the **Subsequent Tasks** column > **Column Settings** > **Edit**. Expand **More Options**, and under **Add additional columns from source list** select **#**. Click Save.

<a class="" data-lightbox="Sharepoint Subsite Creation - Step 8" href="../../../_static/flows/map_sharepoint/map_sharepoint_-_step_8.png" title="Sharepoint Subsite Creation - Step 8" data-title="Sharepoint Subsite Creation - Step 8"><img src="../../../_static/flows/map_sharepoint/map_sharepoint_-_step_8.png" class="align-center" width="800px" height="500px" alt="Sharepoint Subsite Creation - Step 8">
</a>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>To perform the next step you need to access the <a href="https://make.powerautomate.com/environments/Default-a5273f41-687e-4e5e-9fba-18c6ce465b41/flows/shared/f1dd99c5-fc23-47b9-8368-ba816d4137da/details" target="_blank">Job List [Automatic]</a> Flow.
If you do not have access to this Flow, please contact the **programming team** so that a team member can use the **notify.engineering** account to grant access.</p>
</div>

9. Access the <a href="https://make.powerautomate.com/environments/Default-a5273f41-687e-4e5e-9fba-18c6ce465b41/flows/shared/f1dd99c5-fc23-47b9-8368-ba816d4137da/details" target="_blank">Job List [Automatic]</a> Flow and click on edit. Click on the trigger action **When an item is created or modified**, and then in **Site Address** select the subsite you just created. In the next field **List Name** select **Job List**. Click on Save.

<a class="" data-lightbox="Sharepoint Subsite Creation - Step 9" href="../../../_static/flows/map_sharepoint/map_sharepoint_-_step_9.png" title="Sharepoint Subsite Creation - Step 9" data-title="Sharepoint Subsite Creation - Step 9"><img src="../../../_static/flows/map_sharepoint/map_sharepoint_-_step_9.png" class="align-center" width="800px" height="500px" alt="Sharepoint Subsite Creation - Step 9">
</a>

10. Access the <a href="https://make.powerautomate.com/environments/Default-a5273f41-687e-4e5e-9fba-18c6ce465b41/flows/shared/f1dd99c5-fc23-47b9-8368-ba816d4137da/details" target="_blank">Job List [Automatic]</a> Flow and click on edit. Click on the trigger action **When an item is created or modified**, and then in **Site Address** select the subsite you just created. In the next field **List Name** select **Job List**. Click on Save.

<a class="" data-lightbox="Sharepoint Subsite Creation - Step 10" href="../../../_static/flows/map_sharepoint/map_sharepoint_-_step_9.png" title="Sharepoint Subsite Creation - Step 10" data-title="Sharepoint Subsite Creation - Step 10"><img src="../../../_static/flows/map_sharepoint/map_sharepoint_-_step_9.png" class="align-center" width="800px" height="500px" alt="Sharepoint Subsite Creation - Step 10">
</a>