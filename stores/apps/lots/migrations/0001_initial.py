# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Lot'
        db.create_table('lots_lot', (
            ('product_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['inventory.Product'], unique=True, primary_key=True)),
            ('starting_bid', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=2)),
            ('reserve', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=2)),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auctions.AuctionSession'])),
            ('state', self.gf('django.db.models.fields.CharField')(default='A', max_length=1)),
            ('bid_actual', self.gf('django.db.models.fields.related.OneToOneField')(related_name='lot_history', unique=True, null=True, to=orm['lots.BidHistory'])),
        ))
        db.send_create_signal('lots', ['Lot'])

        # Adding model 'ImageLot'
        db.create_table('lots_imagelot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('core.thumbs.ImageWithThumbsField')(max_length=100)),
            ('lot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lots.Lot'])),
            ('primary_picture', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
        ))
        db.send_create_signal('lots', ['ImageLot'])

        # Adding model 'BidHistory'
        db.create_table('lots_bidhistory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lots.Lot'])),
            ('bidder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('bid_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=2)),
            ('bid_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('lots', ['BidHistory'])


    def backwards(self, orm):
        
        # Deleting model 'Lot'
        db.delete_table('lots_lot')

        # Deleting model 'ImageLot'
        db.delete_table('lots_imagelot')

        # Deleting model 'BidHistory'
        db.delete_table('lots_bidhistory')


    models = {
        'auctions.auctionsession': {
            'Meta': {'object_name': 'AuctionSession'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shops.Shop']"}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'inventory.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['market.MarketCategory']"}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latest_item': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shops.Shop']"}),
            'subcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['market.MarketSubCategory']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.ProductType']", 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '11', 'decimal_places': '2'})
        },
        'inventory.producttype': {
            'Meta': {'object_name': 'ProductType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lots.bidhistory': {
            'Meta': {'object_name': 'BidHistory'},
            'bid_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'}),
            'bid_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'bidder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lots.Lot']"})
        },
        'lots.imagelot': {
            'Meta': {'object_name': 'ImageLot'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('core.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'lot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lots.Lot']"}),
            'primary_picture': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'})
        },
        'lots.lot': {
            'Meta': {'object_name': 'Lot', '_ormbases': ['inventory.Product']},
            'bid_actual': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'lot_history'", 'unique': 'True', 'null': 'True', 'to': "orm['lots.BidHistory']"}),
            'product_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['inventory.Product']", 'unique': 'True', 'primary_key': 'True'}),
            'reserve': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auctions.AuctionSession']"}),
            'starting_bid': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'A'", 'max_length': '1'})
        },
        'market.marketcategory': {
            'Meta': {'object_name': 'MarketCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marketplace': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['market.MarketPlace']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '60', 'db_index': 'True'})
        },
        'market.marketplace': {
            'Meta': {'object_name': 'MarketPlace'},
            'base_domain': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '92'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '92', 'db_index': 'True'}),
            'template_prefix': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '92', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '92'})
        },
        'market.marketsubcategory': {
            'Meta': {'unique_together': "(('parent', 'slug'),)", 'object_name': 'MarketSubCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marketplace': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['market.MarketPlace']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'subcategories'", 'null': 'True', 'to': "orm['market.MarketCategory']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '60', 'db_index': 'True'})
        },
        'shops.shop': {
            'Meta': {'object_name': 'Shop'},
            'admin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'bids': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "'39.29038,-76.61219'", 'max_length': '255'}),
            'marketplace': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['market.MarketPlace']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['lots']
