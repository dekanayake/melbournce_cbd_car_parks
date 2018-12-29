var db = connect('127.0.0.1:27017/melbourneCarpark');
db.parking_bays.createIndex( { 'the_geom' : '2dsphere' } );
