import pandas as pd
import glob


files_li = glob.glob("*.csv_processed")#update path here
count = 1
for x in files_li:

	#x='input.csv'
	csv_input = pd.read_csv(x)

	###adding cols
	csv_input['listing_banner_map_marker'] = 'on'
	csv_input['listing_banner_map_type'] = 'ROADMAP'
	csv_input['listing_banner_map_zoom'] = '16'
	csv_input['listing_banner'] = 'banner_map'
	csv_input['listing_inside_view_location'] = ''
	csv_input['listing_inside_view_location_latitude'] = csv_input['lat']
	csv_input['listing_inside_view_location_longitude'] = csv_input['lng']
	csv_input['listing_inside_view_location_zoom'] = '16'
	csv_input['listing_google_street_view_latitude'] = csv_input['lat']
	csv_input['listing_google_street_view_longitude'] = csv_input['lng']
	csv_input['listing_google_street_view_zoom'] = '16'
	csv_input['listing_banner_street_view_latitude'] = csv_input['lat']
	csv_input['listing_banner_street_view_longitude'] = csv_input['lng']
	csv_input['listing_banner_street_view_zoom'] = '16'
	csv_input['post_name'] = csv_input['Name']	# TO assign values of 1 col to new col
	csv_input['listing_description'] = csv_input['Details']	# TO assign values of 1 col to new col
	csv_input['listing_address'] = csv_input['fullAddress']
	csv_input['listing_email'] = csv_input['Mail']
	csv_input['listing_featured_image'] = csv_input['featured_image']
	csv_input['listing_gallery'] = csv_input['Images URL']
	csv_input['listing_map_location'] = csv_input['fullAddress']
	csv_input['listing_map_location_latitude'] = csv_input['lat']
	csv_input['listing_map_location_longitude'] = csv_input['lng']
	csv_input['listing_map_location_zoom'] = '16'
	csv_input['listing_phone'] = csv_input['Phone1']
	csv_input['listing_street_view_location'] = csv_input['fullAddress']
	csv_input['listing_street_view_latitude'] = csv_input['lat']
	csv_input['listing_street_view_longitude'] = csv_input['lng']
 	csv_input['listing_street_view_zoom'] = '16'
	csv_input['listing_street_view_location'] = csv_input['fullAddress']
	csv_input['listing_street_view_location_latitude'] = csv_input['lat']
	csv_input['listing_street_view_location_longitude'] = csv_input['lng']
	csv_input['listing_street_view_location_zoom'] = '16'
 	csv_input['listing_type_metabox'] = csv_input['Services Offered']
 	csv_input['locations'] = csv_input['listing_locations']
  #csv_input['listing_google_address']
	#csv_input['listing_google_map'] = csv_input['Address']
	#csv_input['listing_phone'] 
	#csv_input['listing_inside_view_location']
	#csv_input['listing_map_location'] = csv_input['Address']
	#csv_input['listing_street_view_location']

	csv_input['post_category'] = csv_input['Services Offered']
	csv_input['post_tag'] = csv_input['Services Offered']
	csv_input['listing_categories'] = csv_input['Services Offered']

	###renaming 
	csv_input.rename( columns = {
									'Name'   :  'post_title',
									'Details'  :  'post_content',
									'Mail'   :  'claim_email',
									'listing_person' : 'claim_name',
									'Phone1' : 'claim_phone'
									###phone
									###listing_description
									#'Address'

								}, inplace = True )
	
	print(count)
	count+=1

	csv_input.to_csv(x[:x.find('.csv')]+'_updated.csv', index=False)
