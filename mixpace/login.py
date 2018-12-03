from capability import driver

driver.find_element_by_id('com.mixpace.android.mixpace:id/rbMine').click()
driver.find_element_by_id('com.mixpace.android.mixpace:id/tvHead').click()

driver.find_element_by_id('com.mixpace.android.mixpace:id/phone').send_keys(15300752801)
driver.find_element_by_id('com.mixpace.android.mixpace:id/get_code').click()
driver.find_element_by_id('com.mixpace.android.mixpace:id/check_code').send_keys(111111)
driver.find_element_by_id('com.mixpace.android.mixpace:id/login_or_reg').click()

# driver.find_element_by_id('com.mixpace.android.mixpace:id/ivHead').click()
# driver.find_element_by_id('com.mixpace.android.mixpace:id/ivHead').click()
# driver.find_element_by_id('com.mixpace.android.mixpace:id/tvAlbum').click()
#
# images = driver.find_elements_by_id('com.tencent.gallerymanager:id/img_photo_thumb').click()
# images[2].click()

# driver.find_element_by_id('')









