# Sharepoint Subsite Creation - Setting Up New Xplore Areas

When a new area is created within the Xplore project, it is also necessary to create a new subsite for this new area within the Xplore subsite.

Below is a step-by-step guide on how to do this.

1. Inside the <a href="https://vistacaretech.sharepoint.com/sites/engineering/xplore/_layouts/15/viewlsts.aspx?view=15" target="_blank">Xplore subsite</a>, click on **Site Contents**, then click on **New** and click on **Subsite**. This will redirect you to a new page.

<a data-fancybox="Sharepoint Subsite Creation - Step 1" href="../../../_static/flows/subsite_creation/subsite_creation_step_1.mp4" data-caption="Sharepoint Subsite Creation - Step 1">
  <img src="../../../_static/flows/subsite_creation/subsite_creation_step_1_thumbnail.jpg" alt="Sharepoint Subsite Creation - Step 1" 
      class="align-center" style="width: 700px; height: 400px; cursor: pointer;">
</a>

<br>

2. On the new page, fill in the following fields:

* **Title**: Type the area name followed by the Job Number.

* **Description**: Type Xplore, followed by the area name and the Job Number.

* **URL name**: Type the Job Number.

* **Template Selection**: Select **Team site (no Microsoft 365 group)**.

* **Permissions**: Select **Use same permissions as parent site**.

* **Navigation Inheritance**: Under **Use the top link bar from the parent site?**, select **Yes**.

After filling in the fields, click on **Create** button to be redirected to the newly created subsite.

<a data-fancybox="Sharepoint Subsite Creation - Step 2" href="../../../_static/flows/subsite_creation/subsite_creation_step_2.mp4" data-caption="Sharepoint Subsite Creation - Step 2">
  <img src="../../../_static/flows/subsite_creation/subsite_creation_step_2_thumbnail.jpg" alt="Sharepoint Subsite Creation - Step 2" 
      class="align-center" style="width: 700px; height: 400px; cursor: pointer;">
</a>

<br>

3. In the new subsite, click on **Site Contents**, then click on **Return to classic SharePoint** at the bottom left of the screen to create new lists using pre-made templates.

<a data-fancybox="Sharepoint Subsite Creation - Step 3" href="../../../_static/flows/subsite_creation/subsite_creation_step_3.mp4" data-caption="Sharepoint Subsite Creation - Step 3">
  <img src="../../../_static/flows/subsite_creation/subsite_creation_step_3_thumbnail.jpg" alt="Sharepoint Subsite Creation - Step 3" 
      class="align-center" style="width: 700px; height: 400px; cursor: pointer;">
</a>

<br>

4. Click on **add an app**, then type **Job List** in the search bar and select the app/list called **Job List**. In the window that opens, type **Job List** as the name.

<a data-fancybox="Sharepoint Subsite Creation - Step 4" href="../../../_static/flows/subsite_creation/subsite_creation_step_4.mp4" data-caption="Sharepoint Subsite Creation - Step 4">
  <img src="../../../_static/flows/subsite_creation/subsite_creation_step_4_thumbnail.jpg" alt="Sharepoint Subsite Creation - Step 4" 
      class="align-center" style="width: 700px; height: 400px; cursor: pointer;">
</a>

<br>

5. Click on **add an app** again, type **Task List** in the search bar, select the app/list called **Task List**. In the window that opens type **Task List** as the name.

<a data-fancybox="Sharepoint Subsite Creation - Step 5" href="../../../_static/flows/subsite_creation/subsite_creation_step_5.mp4" data-caption="Sharepoint Subsite Creation - Step 5">
  <img src="../../../_static/flows/subsite_creation/subsite_creation_step_5_thumbnail.jpg" alt="Sharepoint Subsite Creation - Step 5" 
      class="align-center" style="width: 700px; height: 400px; cursor: pointer;">
</a>

<br>

6. Click on **add an app** again, type **Task Capacities** in the search bar, and select **Task Capacities Xplore**. In the window that opens, type **Task Capacities** as the name. After this, you can return to the modern version of SharePoint by clicking on **Exit classic experience** at the bottom left of the screen.

<a data-fancybox="Sharepoint Subsite Creation - Step 6" href="../../../_static/flows/subsite_creation/subsite_creation_step_6.mp4" data-caption="Sharepoint Subsite Creation - Step 6">
  <img src="../../../_static/flows/subsite_creation/subsite_creation_step_6_thumbnail.jpg" alt="Sharepoint Subsite Creation - Step 6" 
      class="align-center" style="width: 700px; height: 400px; cursor: pointer;">
</a>

<br>

7. Access the **Task Capacities** list, click on the **Subsequent Tasks** column > **Column Settings** > **Edit**. In **Select a list as a source**, select **Task Capacities**, then in **Select a column from the list above** select the **Task** column. Click on Save button.

<a data-fancybox="Sharepoint Subsite Creation - Step 7" href="../../../_static/flows/subsite_creation/subsite_creation_step_7.mp4" data-caption="Sharepoint Subsite Creation - Step 7">
  <img src="../../../_static/flows/subsite_creation/subsite_creation_step_7_thumbnail.jpg" alt="Sharepoint Subsite Creation - Step 7" 
      class="align-center" style="width: 700px; height: 400px; cursor: pointer;">
</a>

<br>

8. Again click on the **Subsequent Tasks** column > **Column Settings** > **Edit**. Expand **More Options**, and under **Add additional columns from source list** select **#**. Click on **Save** button.

<a data-fancybox="Sharepoint Subsite Creation - Step 8" href="../../../_static/flows/subsite_creation/subsite_creation_step_8.mp4" data-caption="Sharepoint Subsite Creation - Step 8">
  <img src="../../../_static/flows/subsite_creation/subsite_creation_step_8_thumbnail.jpg" alt="Sharepoint Subsite Creation - Step 8" 
      class="align-center" style="width: 700px; height: 400px; cursor: pointer;">
</a>

<br>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>To perform the next step you need to access the <a href="https://make.powerautomate.com/environments/Default-a5273f41-687e-4e5e-9fba-18c6ce465b41/flows/shared/f1dd99c5-fc23-47b9-8368-ba816d4137da/details" target="_blank">Job List [Automatic]</a> Flow.
If you do not have access, please contact the <b>programming team</b> so that a team member can use the <b>notify.engineering</b> account to grant access.</p>
</div>

9. Access the <a href="https://make.powerautomate.com/environments/Default-a5273f41-687e-4e5e-9fba-18c6ce465b41/flows/shared/f1dd99c5-fc23-47b9-8368-ba816d4137da/details" target="_blank">Job List [Automatic]</a> Flow, click on edit, and click on the trigger action **When an item is created or modified**. In **Site Address**, select the subsite you just created. In **List Name**, select **Job List**. Click on Save button.

<a data-fancybox="Sharepoint Subsite Creation - Step 9" href="../../../_static/flows/subsite_creation/subsite_creation_step_9.mp4" data-caption="Sharepoint Subsite Creation - Step 9">
  <img src="../../../_static/flows/subsite_creation/subsite_creation_step_9_thumbnail.jpg" alt="Sharepoint Subsite Creation - Step 9" 
      class="align-center" style="width: 700px; height: 400px; cursor: pointer;">
</a>

<br>

10. Access the **Job List**, then add the FSAs for the newly created Xplore project area to activate the **Job List [Automatic]** Flow that adds tasks for each FSA in the **Task List**.

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<ul>
  <li><p>You need to add the FSAs in the order you want them to be saved in the <b>Task List</b>.</p></li>
  <li><p><b>Start Date</b> column in the <b>Job List</b> is used as a condition to activate the Flow. Therefore, it is essential to add the date on which the jobs will be started for each FSA.</p></li>
  <li><p>For each FSA, the Flow takes 6 to 8 minutes to add all its tasks to the <b>Task List</b>. The execution time depends on the number of tasks present in the <b>Task Capacities</b>. In any case, the <b>Workflows</b> account should send a message in your <b>Teams</b> informing you when the Flow has started and finished running.</p></li>
</ul>
</div>

<a data-fancybox="Sharepoint Subsite Creation - Step 10" href="../../../_static/flows/subsite_creation/subsite_creation_step_10.mp4" data-caption="Sharepoint Subsite Creation - Step 10">
  <img src="../../../_static/flows/subsite_creation/subsite_creation_step_10_thumbnail.jpg" alt="Sharepoint Subsite Creation - Step 10" 
      class="align-center" style="width: 700px; height: 400px; cursor: pointer;">
</a>

<br>

11.  After the Flow completes and tasks are added for an FSA, indent tasks within their respective groups. Go to the **Task List**, click on **edit**, select tasks related to an FSA using **Shift key**, expand the **Tasks** tab at the top of the screen, and click on **Indent**. Repeat to group tasks.
This way, all the selected items should be moved one level below the item at the top of the list that was not selected.
The same procedure should be repeated to group each group of tasks.

<div class="note">
<p class="admonition-title">TIP</p>
<p> Undo mistakes by selecting incorrectly indented items and clicking <b>Outdent</b> at the top of the screen.</p>
</div>

<a data-fancybox="Sharepoint Subsite Creation - Step 11" href="../../../_static/flows/subsite_creation/subsite_creation_step_11.mp4" data-caption="Sharepoint Subsite Creation - Step 11">
  <img src="../../../_static/flows/subsite_creation/subsite_creation_step_11_thumbnail.jpg" alt="Sharepoint Subsite Creation - Step 11" 
      class="align-center" style="width: 700px; height: 400px; cursor: pointer;">
</a>

<br>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>There is no standard for the types of <b>Permit Lists</b> to be created, since each <b>Job</b> follows its own standard defined by the <b>project leader</b>. Even so, the process for creating <b>Permit Lists</b> shown below remains the same, simply using an existing list that meets the needs of the project in question; otherwise, you will need to create one from scratch.</p>
</div>

12. Go to **Site Contents**, click on **New**, then click on **List**. In the opening window, click on **From existing list**. On the left side of the window, select the site that already has the list to be used as a template. On the right side of the window, select the list to be used as a template.
Change the **Name** of the new list to make it match the related Job. Check the **Show in the site navigation** option and click on **Create**.
Repeat for each **Permit List**.

<a data-fancybox="Sharepoint Subsite Creation - Step 12" href="../../../_static/flows/subsite_creation/subsite_creation_step_12.mp4" data-caption="Sharepoint Subsite Creation - Step 12">
  <img src="../../../_static/flows/subsite_creation/subsite_creation_step_12_thumbnail.jpg" alt="Sharepoint Subsite Creation - Step 12" 
      class="align-center" style="width: 700px; height: 400px; cursor: pointer;">
</a>

<br>

13. Configure the new subsite navigation layout: Go to **Site Contents** and click on **Site Settings** in the top right of the screen. Click **Navigation** under **Look and Feel**. Select **Display the same navigation items as the parent site** for both **Global Navigation** and **Current Navigation**. Use the panel buttons in **Structural Navigation: Editing and Sorting** to remove unnecessary links, add missing links, and sort them. Keep links to **Documents**, **Permit Lists**, **Task List**, and **Site contents**. Finally, click on **OK** button.

<a data-fancybox="Sharepoint Subsite Creation - Step 13" href="../../../_static/flows/subsite_creation/subsite_creation_step_13.mp4" data-caption="Sharepoint Subsite Creation - Step 13">
  <img src="../../../_static/flows/subsite_creation/subsite_creation_step_13_thumbnail.jpg" alt="Sharepoint Subsite Creation - Step 13" 
      class="align-center" style="width: 700px; height: 400px; cursor: pointer;">
</a>

<br>