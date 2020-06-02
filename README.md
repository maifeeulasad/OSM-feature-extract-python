# OSM-feature-extract-python
feature extractor like road,path,motorway all belongs to highway and so on, just helps to classify features


For API like usage : [API - features](https://raw.githubusercontent.com/maifeeulasad/OSM-feature-extract-python/master/features.json). Use simple GET.

Current result :
```
{
  "fire_object:type": [],
  "sorting_name": [],
  "highway": [
    "motorway",
    "trunk",
    "primary",
    "secondary",
    "tertiary",
    "unclassified",
    "residential",
    "motorway_link",
    "trunk_link",
    "primary_link",
    "secondary_link",
    "tertiary_link",
    "living_street",
    "service",
    "pedestrian",
    "track",
    "bus_guideway",
    "escape",
    "raceway",
    "road",
    "footway",
    "bridleway",
    "steps",
    "corridor",
    "path",
    "cycleway",
    "proposed",
    "construction",
    "bus_stop",
    "crossing",
    "elevator",
    "emergency_access_point",
    "give_way",
    "milestone",
    "mini_roundabout",
    "motorway_junction",
    "passing_place",
    "platform",
    "rest_area",
    "speed_camera",
    "street_lamp",
    "services",
    "stop",
    "traffic_mirror",
    "traffic_signals",
    "trailhead",
    "turning_circle",
    "turning_loop",
    "toll_gantry",
    "User Defined"
  ],
  "non_existent_levels": [],
  "wood": [],
  "junction": [
    "roundabout"
  ],
  "building": [
    "apartments",
    "bungalow",
    "cabin",
    "detached",
    "dormitory",
    "farm",
    "ger",
    "hotel",
    "house",
    "houseboat",
    "residential",
    "semidetached_house",
    "static_caravan",
    "terrace",
    "commercial",
    "industrial",
    "kiosk",
    "office",
    "retail",
    "supermarket",
    "warehouse",
    "cathedral",
    "chapel",
    "church",
    "mosque",
    "religious",
    "shrine",
    "synagogue",
    "temple",
    "bakehouse",
    "civic",
    "fire_station",
    "government",
    "hospital",
    "kindergarten",
    "public",
    "school",
    "toilets",
    "train_station",
    "transportation",
    "university",
    "barn",
    "conservatory",
    "cowshed",
    "farm_auxiliary",
    "greenhouse",
    "stable",
    "sty",
    "grandstand",
    "pavilion",
    "riding_hall",
    "sports_hall",
    "stadium",
    "hangar",
    "hut",
    "shed",
    "carport",
    "garage",
    "garages",
    "parking",
    "digester",
    "service",
    "transformer_tower",
    "water_tower",
    "bunker",
    "bridge",
    "construction",
    "roof",
    "ruins",
    "tree_house",
    "user defined "
  ],
  "service": [
    "alley",
    "crossover",
    "siding",
    "spur",
    "yard"
  ],
  "est_width": [],
  "toll": [],
  "addr:place": [],
  "area": [],
  "cutting": [
    "yes"
  ],
  "bicycle_road": [],
  "motorcycle": [],
  "wheelchair": [],
  "reg_name": [],
  "sac_scale": [],
  "opening_hours": [],
  "psv": [],
  "ele": [],
  "goods": [],
  "shop": [
    "alcohol",
    "bakery",
    "beverages",
    "brewing_supplies",
    "butcher",
    "cheese",
    "chocolate",
    "coffee",
    "confectionery",
    "convenience",
    "deli",
    "dairy",
    "farm",
    "frozen_food",
    "greengrocer",
    "health_food",
    "ice_cream",
    "organic",
    "pasta",
    "pastry",
    "seafood",
    "spices",
    "tea",
    "wine",
    "water",
    "department_store",
    "general",
    "kiosk",
    "mall",
    "supermarket",
    "wholesale",
    "baby_goods",
    "bag",
    "boutique",
    "clothes",
    "fabric",
    "fashion",
    "fashion_accessories",
    "jewelry",
    "leather",
    "sewing",
    "shoes",
    "tailor",
    "watches",
    "wool",
    "charity",
    "second_hand",
    "variety_store",
    "beauty",
    "chemist",
    "cosmetics",
    "erotic",
    "hairdresser",
    "hairdresser_supply",
    "hearing_aids",
    "herbalist",
    "massage",
    "medical_supply",
    "nutrition_supplements",
    "optician",
    "perfumery",
    "tattoo",
    "agrarian",
    "appliance",
    "bathroom_furnishing",
    "doityourself",
    "electrical",
    "energy",
    "fireplace",
    "florist",
    "garden_centre",
    "garden_furniture",
    "gas",
    "glaziery",
    "hardware",
    "houseware",
    "locksmith",
    "paint",
    "security",
    "trade",
    "windows",
    "antiques",
    "bed",
    "candles",
    "carpet",
    "curtain",
    "doors",
    "flooring",
    "furniture",
    "household_linen",
    "interior_decoration",
    "kitchen",
    "lighting",
    "tiles",
    "window_blind",
    "computer",
    "robot",
    "electronics",
    "hifi",
    "mobile_phone",
    "radiotechnics",
    "vacuum_cleaner",
    "atv",
    "bicycle",
    "boat",
    "car",
    "car_repair",
    "car_parts",
    "caravan",
    "fuel",
    "fishing",
    "free_flying",
    "golf",
    "hunting",
    "jetski",
    "military_surplus",
    "motorcycle",
    "outdoor",
    "scuba_diving",
    "ski",
    "snowmobile",
    "sports",
    "swimming_pool",
    "trailer",
    "tyres",
    "art",
    "collector",
    "craft",
    "frame",
    "games",
    "model",
    "music",
    "musical_instrument",
    "photo",
    "camera",
    "trophy",
    "video",
    "video_games",
    "anime",
    "books",
    "gift",
    "lottery",
    "newsagent",
    "stationery",
    "ticket",
    "bookmaker",
    "cannabis",
    "copyshop",
    "dry_cleaning",
    "e-cigarette",
    "funeral_directors",
    "laundry",
    "money_lender",
    "party",
    "pawnbroker",
    "pet",
    "pet_grooming",
    "pest_control",
    "pyrotechnics",
    "religion",
    "storage_rental",
    "tobacco",
    "toys",
    "travel_agency",
    "vacant",
    "weapons",
    "outpost",
    "user defined"
  ],
  "official_name": [],
  "traffic_sign": [],
  "tactile_paving": [],
  "forestry": [],
  "maxwidth": [
    "Width"
  ],
  "surface": [],
  "amenity": [
    "bar",
    "bbq",
    "biergarten",
    "cafe",
    "drinking_water",
    "fast_food",
    "food_court",
    "ice_cream",
    "pub",
    "restaurant",
    "college",
    "driving_school",
    "kindergarten",
    "language_school",
    "library",
    "toy_library",
    "music_school",
    "school",
    "university",
    "bicycle_parking",
    "bicycle_repair_station",
    "bicycle_rental",
    "boat_rental",
    "boat_sharing",
    "bus_station",
    "car_rental",
    "car_sharing",
    "car_wash",
    "vehicle_inspection",
    "charging_station",
    "ferry_terminal",
    "fuel",
    "grit_bin",
    "motorcycle_parking",
    "parking",
    "parking_entrance",
    "parking_space",
    "taxi",
    "atm",
    "bank",
    "bureau_de_change",
    "baby_hatch",
    "clinic",
    "dentist",
    "doctors",
    "hospital",
    "nursing_home",
    "pharmacy",
    "social_facility",
    "veterinary",
    "arts_centre",
    "brothel",
    "casino",
    "cinema",
    "community_centre",
    "fountain",
    "gambling",
    "nightclub",
    "planetarium",
    "public_bookcase",
    "social_centre",
    "stripclub",
    "studio",
    "swingerclub",
    "theatre",
    "animal_boarding",
    "animal_shelter",
    "baking_oven",
    "bench",
    "childcare",
    "clock",
    "conference_centre",
    "courthouse",
    "crematorium",
    "dive_centre",
    "embassy",
    "fire_station",
    "firepit",
    "give_box",
    "grave_yard",
    "gym",
    "hunting_stand",
    "internet_cafe",
    "kitchen",
    "kneipp_water_cure",
    "marketplace",
    "monastery",
    "photo_booth",
    "place_of_worship",
    "police",
    "post_box",
    "post_depot",
    "post_office",
    "prison",
    "public_bath",
    "public_building",
    "ranger_station",
    "recycling",
    "refugee_site",
    "sanitary_dump_station",
    "sauna",
    "shelter",
    "shower",
    "telephone",
    "toilets",
    "townhall",
    "vending_machine",
    "waste_basket",
    "waste_disposal",
    "waste_transfer_station",
    "watering_place",
    "water_point",
    "user defined"
  ],
  "name:left": [],
  "disused": [],
  "toilets:wheelchair": [],
  "mtb:scale:uphill": [],
  "leaf_type": [],
  "maxspeed": [
    "Speed"
  ],
  "ice_road": [],
  "building:max_level": [],
  "location": [],
  "fire_rank": [],
  "nudism": [],
  "public_transport": [
    "stop_position",
    "platform",
    "station"
  ],
  "drive_through": [],
  "loc_name": [],
  "roadtrain": [],
  "railway:track_ref": [],
  "mtb:description": [],
  "motor_vehicle": [],
  "addr:street": [],
  "short_name": [],
  "produce": [],
  "overtaking": [],
  "bdouble": [],
  "oneway": [],
  "passing_places": [],
  "name": [],
  "parking:lane": [],
  "motorcar": [],
  "cycleway": [
    "lane",
    "opposite",
    "opposite_lane",
    "track",
    "opposite_track",
    "share_busway",
    "opposite_share_busway",
    "shared_lane"
  ],
  "admin_level": [],
  "maxlength": [
    "Length"
  ],
  "turn": [],
  "tracks": [],
  "incline": [],
  "width": [],
  "hgv": [],
  "moped": [],
  "name:": [],
  "hazmat": [],
  "mofa": [],
  "int_name": [],
  "addr:interpolation": [],
  "atv": [],
  "boundary": [
    "aboriginal_lands",
    "administrative",
    "maritime",
    "marker",
    "national_park",
    "political",
    "postal_code",
    "protected_area",
    "user defined"
  ],
  "addr:hamlet": [],
  "mtb:scale": [],
  "inscription": [],
  "railway": [
    "abandoned",
    "construction",
    "disused",
    "funicular",
    "light_rail",
    "miniature",
    "monorail",
    "narrow_gauge",
    "preserved",
    "rail",
    "subway",
    "tram",
    "halt",
    "platform",
    "station",
    "subway_entrance",
    "tram_stop",
    "buffer_stop",
    "derail",
    "crossing",
    "level_crossing",
    "signal",
    "switch",
    "railway_crossing",
    "turntable",
    "roundhouse",
    "traverser",
    "wash",
    "user defined"
  ],
  "voltage": [],
  "ski": [],
  "addr:city": [],
  "tank": [],
  "maxstay": [],
  "foot": [],
  "building:min_level": [],
  "frequency": [],
  "emergency": [
    "phone"
  ],
  "addr:postcode": [],
  "old_name": [],
  "name_1": [],
  "maxweight": [
    "Weight"
  ],
  "bridge": [
    "yes"
  ],
  "embedded_rails": [],
  "nat_name": [],
  "building:levels": [],
  "layer": [],
  "parking:condition": [],
  "addr:full": [],
  "agricultural": [],
  "Relation:restriction": [],
  "golf_cart": [],
  "crossing": [],
  "route": [
    "bicycle",
    "bus",
    "canoe",
    "detour",
    "ferry",
    "foot",
    "hiking",
    "horse",
    "inline_skates",
    "light_rail",
    "mtb",
    "piste",
    "power",
    "railway",
    "road",
    "running",
    "ski",
    "subway",
    "train",
    "tracks",
    "tram",
    "trolleybus",
    ""
  ],
  "crossing:island": [],
  "landuse": [
    "commercial",
    "construction",
    "industrial",
    "residential",
    "retail",
    "allotments",
    "farmland",
    "farmyard",
    "forest",
    "meadow",
    "orchard",
    "vineyard",
    "basin",
    "brownfield",
    "cemetery",
    "conservation",
    "depot",
    "garages",
    "grass",
    "greenfield",
    "greenhouse_horticulture",
    "landfill",
    "military",
    "",
    "plant_nursery",
    "port",
    "quarry",
    "railway",
    "recreation_ground",
    "religious",
    "reservoir",
    "salt_pond",
    "village_green",
    "user defined",
    "railway"
  ],
  "tunnel": [
    "yes"
  ],
  "addr:housenumber": [],
  "mountain_pass": [],
  "maxaxleload": [
    "Weight"
  ],
  "charge": [],
  "abutters": [],
  "tracktype": [],
  "start_date": [],
  "narrow": [],
  "lanes": [],
  "ford": [],
  "tidal": [],
  "smoothness": [],
  "driving_side": [],
  "building:fireproof": [],
  "addr:state": [],
  "usage": [],
  "winter_road": [],
  "boat": [],
  "addr:subdistrict": [],
  "access": [
    "designated"
  ],
  "drive_in": [],
  "addr:suburb": [],
  "bicycle": [],
  "entrance": [],
  "internet_access": [],
  "sidewalk": [],
  "addr:housename": [],
  "motorboat": [],
  "mtb:scale:imba": [],
  "motorroad": [],
  "addr:province": [],
  "noexit": [],
  "horse": [],
  "4wd_only": [],
  "vehicle": [],
  "addr:district": [],
  "lhv": [],
  "building:flats": [],
  "inline_skates": [],
  "busway": [
    "lane"
  ],
  "maxheight": [
    "Height"
  ],
  "end_date": [],
  "service_times": [],
  "leaf_cycle": [],
  "addr:inclusion": [],
  "electrified": [],
  "minspeed": [
    "Speed"
  ],
  "addr:country": [],
  "traffic_calming": [],
  "alt_name": [],
  "soft_storey": [],
  "border_type": [],
  "embankment": [],
  "trail_visibility": [],
  "addr:conscriptionnumber": [],
  "fire_operator": [],
  "height": [],
  "lit": [],
  "covered": [],
  "addr:flats": [],
  "operator": []
}
```
