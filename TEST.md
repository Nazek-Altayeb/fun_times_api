# API Test Guide

The testing.md file provides an overview of the testing conducted on Fun times API. 
It covers code validation, accessibility, performance, testing on various devices, browser compatibility, testing user stories, and user feedback and improvements. 
Each section describes the tools used.

## Table of Content

- [API Test Guide](#api-test-guide)
  - [Table of Content](#table-of-content)
    - [Code Validation](#code-validation)
    - [Automated test](#automated-test)
    - [Manual test](#manual-test)
      - [URL Testing](#url-testing)
      - [CRUD functionality](#crud-functionality)

### Code Validation

The py files have been validated by [PEP 8](https://pep8ci.herokuapp.com/), 
it examines the the code format, so it ensures the consistency and readability.
here below are lists of results of the pep8 test that has been performed against the py files.

**fun times api**

| **Tested** | **Result** | **View Result** 
--- | --- | --- 
|serializers|No errors|<details><summary>Screenshot of result</summary>![Result](https://res.cloudinary.com/nazek/image/upload/v1696695101/fun_times_api-_serializer_sfxlqw.png)</details>
|settings|No errors|<details><summary>Screenshot of result</summary>![Result](https://res.cloudinary.com/nazek/image/upload/v1696695101/fun_times_api_-_setting_movbvv.png)</details>
|urls|No errors|<details><summary>Screenshot of result</summary>![Result](https://res.cloudinary.com/nazek/image/upload/v1696695101/fun_times_api_-_urls_aktyqs.png)</details>
|views|No errors|<details><summary>Screenshot of result</summary>![Result](https://res.cloudinary.com/nazek/image/upload/v1696695101/fun_times_api_-_views_a1alyh.png)</details>

**adventures list**

| **Tested** | **Result** | **View Result** 
--- | --- | --- 
|models|No errors|[Result](https://res.cloudinary.com/nazek/image/upload/v1696695637/adventures_-_model_yqhwse.png)
|serializers|No errors|[Result](https://res.cloudinary.com/nazek/image/upload/v1696695637/adventures_-_serializer_klvglg.png)
|urls|No errors|[Result](https://res.cloudinary.com/nazek/image/upload/v1696695636/adventures_-_url_yrlhhw.png)
|views|No errors|[Result](https://res.cloudinary.com/nazek/image/upload/v1696695637/adventures_-_view_vipxeu.png)

**comments**

| **Tested** | **Result** | **View Result**
--- | --- | --- 
|models|No errors|[Result](https://res.cloudinary.com/nazek/image/upload/v1696695923/comments_-_model_t6buet.png)
|serializers|No errors|[Result](https://res.cloudinary.com/nazek/image/upload/v1696695922/comments_serializers_qzztmk.png)
|urls|No errors|[Result](https://res.cloudinary.com/nazek/image/upload/v1696695922/commants_urls_ou2kg1.png)
|views|No errors|[Result](https://res.cloudinary.com/nazek/image/upload/v1696695923/coments_-_views_bm0fyy.png)

**followers**

| **Tested** | **Result** | **View Result** 
--- | --- | --- 
|models|No errors|[Result](https://res.cloudinary.com/nazek/image/upload/v1696696186/followers_-_model_xrb8cq.png)
|serializers||[Result](https://res.cloudinary.com/nazek/image/upload/v1696696186/followers_-_serializer_fp8io9.png)
|urls|No errors|[Result](https://res.cloudinary.com/nazek/image/upload/v1696696185/followers_-_url_cwt7dl.png)
|views|No errors|[Result](https://res.cloudinary.com/nazek/image/upload/v1696696185/followers_-_views_pakwsq.png)

**likes**

| **Tested** | **Result** | **View Result** 
--- | --- | --- 
|models|No errors|[Result](https://res.cloudinary.com/nazek/image/upload/v1696696398/likes_-_model_f7gcbo.png)
|merializers|No errors|[Result](https://res.cloudinary.com/nazek/image/upload/v1696696398/likes_-_serializers_igviwj.png)
|urls|No errors|[Result](https://res.cloudinary.com/nazek/image/upload/v1696696398/likes_-_urls_us6lwz.png)
|views|No errors|[Result](https://res.cloudinary.com/nazek/image/upload/v1696696398/likes_-_views_v06bys.png)

**posts**

| **Tested** | **Result** | **View Result**
--- | --- | --- 
|models|No errors|[Result](https://res.cloudinary.com/nazek/image/upload/v1696696633/posts_-_model_wmbitz.png)
|serializers|No errors|[Result](https://res.cloudinary.com/nazek/image/upload/v1696696632/posts_-_serializers_sogtbn.png)
|urls|No errors|[Result](https://res.cloudinary.com/nazek/image/upload/v1696696632/posts_-_url_yorx14.png)
|views|No errors|[Result](https://res.cloudinary.com/nazek/image/upload/v1696696632/posts_-_views_swftlr.png)

**profiles**

| **Tested** | **Result** | **View Result** 
--- | --- | --- 
|models|No errors|[Result](https://res.cloudinary.com/nazek/image/upload/v1696696974/profiles_-_model_zy9jis.png)
|serializers|No errors|[Result](https://res.cloudinary.com/nazek/image/upload/v1696696974/profiles_-_serializer_isou49.png)
|urls|No errors|[Result](https://res.cloudinary.com/nazek/image/upload/v1696696974/profiles_-_url_xisqko.png)
|views|No errors|[Result](https://res.cloudinary.com/nazek/image/upload/v1696696974/profiles_-_views_dbpwed.png)


### Automated test

### Manual test

The manaul test is perfomed by following the below


1. Check all CRUD Functionalities for the different entities (profiles, posts, adventureslist, comments, followers, likes) , and test by appling these functionalities on exammples, check the results in the database to make sure data is stored/removed/updated there correctly 

2. Test the search functionality, by typing existing filters (post title, content ... etc) and try the opposite as well.
3. Test the paths, make sure all used pathed are connected with methods that perform the expected functionality.

#### URL Testing

| **Tested** | **Expected result** | **Result** 
--- | --- | --- 
|Root URL|Show welcome message|Works as expected
|/adventureslist|Display Bookmarked posts |Works as expected
|/adventureslist/{id}|Display Bookmarked post details|Works as expected
|/posts|Display posts list |Works as expected
|/posts/{id}|Display posts detail|Works as expected
|/comments|Display comments list |Works as expected
|/comments/{id}|Display comment detail|Works as expected
|/likes|Display likes list |Works as expected
|/likes/{id}|Display like detail|Works as expected
|/profiles|Display profiles list |Works as expected
|/profiles/{id}|Display profiles detail|Works as expected
|/followers|Display followers list |Works as expected
|/followers/{id}|Display follower detail|Works as expected


#### CRUD functionality

| **Tested** | **Create** | **View** | **Update** | **Delete** |
--- | --- | --- | :---:| :---:
|Profile|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:
|Post|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:
|Comment|:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:
|Like|:white_check_mark:|:white_check_mark:|-|:white_check_mark:
|Follow|:white_check_mark:|:white_check_mark:|-|:white_check_mark:
|Adventureslist|:white_check_mark:|:white_check_mark:|-|:white_check_mark:



