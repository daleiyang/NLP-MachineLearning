/**
 * @fileoverview Provides common functionality for HTML5 layouts.
 */


/**
 * Height of the vertical layouts. Units are pixels.
 * @type {number}
 */
var HORIZONTAL_LAYOUTS_HEIGHT = 90;


/**
 * Layout shape type.
 * @type {string}
 */
var HORIZONTAL_TYPE = 'horizontal';


/**
 * Parts of the user agent value, which are used to detect IE.
 * @enum {string}
 */
var ieUserAgentPart = {
  IE_V11_AND_ABOVE: 'trident/',
  IE_BELOW_V11: 'msie'
};


/**
 * Height of 320x50 layout size. Units are pixels.
 * @type {number}
 */
var LAYOUT_HEIGHT_320X50 = 50;


/**
 * Height of 320x100 layout size. Units are pixels.
 * @type {number}
 */
var LAYOUT_HEIGHT_320X100 = 100;


/**
 * Height of 468x60 layout size. Units are pixels.
 * @type {number}
 */
var LAYOUT_HEIGHT_468X60 = 60;


/**
 * Maximun padding that can be set to the logo. Units are pixels.
 * @type {number}
 */
var MAX_LOGO_PADDING = 20;


/**
 * Minimum font size of product price. Units are pixels.
 * @type {number}
 */
var MIN_FONT_SIZE = 7;


/**
 * Minimum padding that can be set to the logo. Units are pixels.
 * @type {number}
 */
var MIN_LOGO_PADDING = 0;


/**
 * Minimum pixel size of the logo. Units are pixels.
 * @type {number}
 */
var MIN_LOGO_SIZE = 20;


/**
 * Layout shape type.
 * @type {string}
 */
var MIN_TYPE = 'minimal';


/**
 * Regular expressions to parse HEX color.
 * @enum {RegExp}
 */
var RgbChannelsRegExps = {
  /** Returns hex representation of every channel of the color. */
  FULL: /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i,
  /** Returns symbols that represent channels. */
  SHORT: /^#?([a-f\d])([a-f\d])([a-f\d])$/i
};


/**
 * Star rating constants.
 * @enum {number}
 */
var StarRating = {
  /** Maximum star rating number to show. */
  MAX: 5,
  /** Maximum rating delta to show a half of a star. */
  MAX_DELTA: .71,
  /** Minimum star rating to show stars. */
  MIN: 3,
  /** Minimum rating delta to show a half of a star. */
  MIN_DELTA: .29
};


/**
 * Layout shape type.
 * @type {string}
 */
var SQUARE_TYPE = 'square';


/**
 * Height of the vertical layouts. Units are pixels.
 * @type {number}
 */
var VERTICAL_LAYOUTS_HEIGHT = 600;


/**
 * Layout shape type.
 * @type {string}
 */
var VERTICAL_TYPE = 'vertical';


/**
 * Utils object with common functionality for the layouts.
 * @return {!Object.<function>} Globally available functions.
 */
var helpers = (function() {
  var utilsModule = angular.module('utils');


  /**
   * Controller for using data binding in layout.
   * @param {Object} $scope AngularJS layout $scope.
   * @param {Object} dynamicData Dynamic data from DAB.
   */
  function LayoutController($scope, dynamicData) {
    $scope.data = dynamicData.google_template_data.adData[0];
    $scope.frameHeight = dynamicData.google_height;
    $scope.fieldReference = '';

    $scope.products = utils.parse($scope.data, 'Product').slice(0);
    $scope.headline = utils.parse($scope.data, 'Headline')[0];
    $scope.design = utils.parse($scope.data, 'Design')[0];

    if ($scope.design.priceSize < MIN_FONT_SIZE) {
      $scope.design.priceSize = MIN_FONT_SIZE;
    }
    if ($scope.design.nameSize < MIN_FONT_SIZE) {
      $scope.design.nameSize = MIN_FONT_SIZE;
    }
    if ($scope.design.headlineSize < MIN_FONT_SIZE) {
      $scope.design.headlineSize = MIN_FONT_SIZE;
    }
    if ($scope.design.descriptionSize < MIN_FONT_SIZE) {
      $scope.design.descriptionSize = MIN_FONT_SIZE;
    }

    switch (parseInt($scope.frameHeight, 10)) {
      case VERTICAL_LAYOUTS_HEIGHT:
        $scope.layoutType = VERTICAL_TYPE;
        break;
      case LAYOUT_HEIGHT_468X60:
      case HORIZONTAL_LAYOUTS_HEIGHT:
        $scope.layoutType = HORIZONTAL_TYPE;
        break;
      case LAYOUT_HEIGHT_320X50:
      case LAYOUT_HEIGHT_320X100:
        $scope.layoutType = MIN_TYPE;
        break;
      default:
        $scope.layoutType = SQUARE_TYPE;
    }


    /**
     * Checks whether the given image has already been loaded.
     * @param {string} url Image source URL.
     * @return {boolean} Whether the given URL is in preloaded images list.
     */
    $scope.checkUrl = function(url) {
      if (!url || url == 'empty') {
        return false;
      }
      return utils.isLoadedRes(url);
    };


    /**
     * Verifies if the star rating should be shown.
     * @param {string} rating Rating value.
     * @return {boolean} If the star rating should be shown.
     */
    $scope.isRatingValid = function(rating) {
      return $scope.isTrulyNumber(rating) &&
          parseFloat(rating) >= StarRating.MIN;
    };


    /**
     * Verifies whether the rating should have half stars. According to Google
     * Rating all the ratings with remainders between .29 and .71 should show
     * half stars.
     * @param {string=} opt_rating Star rating as a string.
     * @return {boolean} If the star rating is between .29 and .71, and should
     * show half of a star.
     */
    $scope.isShownHalf = function(opt_rating) {
      opt_rating = opt_rating || 0;
      var floor = Math.floor(parseFloat(opt_rating));

      // Don't show half star for rating more than {@code StarRating.MAX} or
      // equals.
      if (floor >= StarRating.MAX) {
        return false;
      }
      var mod = opt_rating % floor;
      return mod > StarRating.MIN_DELTA ? mod < StarRating.MAX_DELTA : false;
    };


    /**
     * Builds array of the star for the rating.
     * @param {number} rating Rating value.
     * @return {Array.<number>} Array of the rating stars.
     */
    $scope.starRatingArray = function(rating) {
      if ($scope.isRatingValid(rating)) {
        var floorRating = parseFloat(rating);
        if (floorRating > StarRating.MAX) {
          rating = StarRating.MAX;
        }
      } else {
        rating = 0;
      }

      return new Array(ratingToInteger(rating));
    };


    /**
     * Verifies if the passed parameter maybe converted to text.
     * @param {string} numString The string to verify.
     * @return {boolean} Returns true if the string can be converted to number.
     */
    $scope.isTrulyNumber = function(numString) {
      return !!Number(numString);
    };


    /**
     * Verifies if the string from DAB is really empty.
     * @param {string} str String to verify.
     * @return {boolean} Returns true if the string is empty.
     */
    $scope.isEmpty = function(str) {
      if (!str) {
        return true;
      }
      str = str.trim();
      return !str || !str.length;
    };


    /**
     * Converts string from DAB to boolean. DAB provides true or false in
     * uppercase.
     * @param {string} str String to convert.
     * @return {boolean} Boolean representation of the string provided.
     */
    $scope.toBoolean = function(str) {
      if (!str) {
        return false;
      }
      return str.toLowerCase() === 'true';
    };

    var prodClickOnly = $scope.toBoolean($scope.headline.productClickOnly);

    if ($scope.products.length && $scope.products[0].url) {
      $scope.fieldReference = prodClickOnly ? 'Product_0_url' : '';
      $scope.currentProductIndex = 0;
    }

    $scope.$on('urlchange', function(e, index) {
      var currentIndex = parseInt(index, 10);
      $scope.$apply(function() {
        $scope.fieldReference = !isNaN(currentIndex) ?
            'Product_' + currentIndex + '_url' : '';

        if (!isNaN(currentIndex)) {
          $scope.currentProductIndex = currentIndex;
        }
      });
    });


    /**
     * Builds lists of the products to be used in the carousels.
     * @param {number} maxItems Maximum number of items in the list.
     * @param {number} maxLists Maximum number of lists.
     * @return {Array.<Object>} All the products lists available.
     */
    $scope.buildProductLists = function(maxItems, maxLists) {
      var res = [];
      var products = $scope.products;
      var chunk = maxItems || 4;
      var max = maxLists || 10;
      for (var i = 0, j = 0; i < products.length && j++ < max; i += chunk) {
        var list = products.slice(i, i + chunk);
        list = list.concat(products.slice(0, chunk - list.length));
        res.push(list);
      }
      return res;
    };


    /**
     * Shades given color.
     * @param {string} color Color to shade.
     * @param {number} percent Percentage to shade.
     * @return {string} Updated color.
     */
    $scope.shadeColor = function(color, percent) {
      var f = parseInt(color.slice(1), 16),
          t = percent < 0 ? 0 : 255,
          p = percent < 0 ? percent * -1 : percent,
          R = f >> 16,
          G = f >> 8 & 0x00FF,
          B = f & 0x0000FF;

      return '#' +
          (0x1000000 + (Math.round((t - R) * p) + R) *
          0x10000 + (Math.round((t - G) * p) + G) *
          0x100 + (Math.round((t - B) * p) + B)).toString(16).slice(1);
    };


    /**
     * Changes the brightness of the color using its RGBA representation.
     * @param {string} color The color to change.
     * @param {number} delta Percentage to change the brightness of the color.
     * @param {number=} opt_alpha Alpha channel of the color.
     * @return {?string} Updated color in RGBA.
     */
    $scope.changeBrightnessRGBA = function(color, delta, opt_alpha) {
      var alpha = opt_alpha || 0;
      var hex = getFullHexColor(color.toColor());
      var result = RgbChannelsRegExps.FULL.exec(hex);
      var rgb = '', part;
      for (var i = 1; i < result.length; i++) {
        part = parseInt(result[i], 16);
        part += part * delta;
        rgb += Math.round(Math.min(Math.max(0, part), 255)) + ',';
      }

      return rgb ? 'rgba(' + rgb + alpha + ')' : null;
    };
  }


  /**
   * Sets last product the user had interaction with. By default, the user exits
   * to product with index 0 if the {@code prodClickOnly} is set to true, and to
   * destination URL if the {@code prodClickOnly} is set to false.
   * @return {!angular.Directive} Directive definition object.
   */
  utilsModule.directive('interaction', function() {
    return {
      restrict: 'A',
      link: function(scope, el, attrs) {
        var prodClickOnly = scope.toBoolean(scope.headline.productClickOnly);

        el.bind('mouseover', function() {
          scope.$emit(attrs.interaction, attrs.productIndex);
        });

        if (!prodClickOnly) {
          el.bind('mouseleave', function() {
            scope.$emit(attrs.interaction, '');
          });
        }
      }
    };
  });


  /**
   * Exposes observedImageFit as a custom attribute to set watcher
   * for layouts with image pre-loading and carousel.
   * @return {!angular.Directive} Directive definition object.
   */
  utilsModule.directive('observedImageFit', function() {
    return {
      restrict: 'A',
      link: function(scope, el, attr) {
        var srcLoc = attr.loc;
        var done = false;
        scope.$watch(srcLoc, function() {
          if (!done) {
            var src = scope.$eval(srcLoc);
            if (scope.checkUrl(src)) {
              new ddab.layouts.utils.DynamicImageFit(el[0], src, attr.scaletype,
                  attr.aligntype);
            }
            done = true;
          }
        });
      }
    };
  });


  /**
   * Exposes exitTrigger as a custom attribute to prevent
   * anchor exit for the carousels.
   * @return {!angular.Directive} Directive definition object.
   */
  utilsModule.directive('exitTrigger', function() {
    return {
      restrict: 'A',
      link: function(scope, el) {
        el.bind('click', function(e) {
          if (scope.noTrigger) {
            e.preventDefault();
            scope.noTrigger = false;
          }
        });
      }
    };
  });


  /**
   * Exposes extTextFit as a custom attribute to prevent
   * anchor exit for the carousels.
   * @param {!angular.$timeout} $timeout The Angular timeout service.
   * @return {!angular.Directive} Directive definition object.
   */
  utilsModule.directive('extTextFit', function($timeout) {
    return {
      restrict: 'A',
      link: function(scope, el) {
        $timeout(function() {
          extTextFit(el);
        });
      }
    };
  });


  /**
   * Exposes dynamicStyles as a custom attribute. Handles the dynamic styles and
   * adds them to the document. Workaround for angular not binding data for
   * style tag.
   * @param {!angular.$timeout} $timeout The Angular timeout service.
   * @return {!angular.Directive} Directive definition object.
   */
  utilsModule.directive('dynamicStyle', ['$timeout', function($timeout) {
    return {
      restrict: 'A',
      link: function(scope, element) {
        // TODO: Find more optimized solution. Any change here causes endless
        // loop for the layouts.
        $timeout(function() {
          var el = element[0];
          var styleEl = document.createElement('style');
          styleEl.innerHTML = el.textContent;
          document.getElementsByTagName('head')[0].appendChild(styleEl);
          el.innerHTML = '';
        });
      }
    };
  }]);


  /**
   * Exposes logoFit as a custom attribute. Handles logo, if available. Adds
   * padding to the logo.
   * @return {!angular.Directive} Directive definition object.
   */
  utilsModule.directive('logoFit', function() {
    return {
      restrict: 'A',
      link: function(scope, element, attrs) {
        var done = false;
        scope.$watch(attrs.loc, function() {
          if (!done) {
            var el = element[0];
            var src = scope.$eval(attrs.loc);

            if (scope.checkUrl(src)) {
              setTimeout(function() {
                var data = scope.design['logoPadding'] || 0;
                var logoMargins = utils.logoMargin(element);
                var padding = parseInt(data);
                var parent = element.parent();
                padding = Math.min(Math.max(MIN_LOGO_PADDING,
                    padding), MAX_LOGO_PADDING);
                var img;
                utils.preload(src, function(image) {
                  img = image;
                });
                var imgRatio = img.width / img.height;
                var minLogoSize = imgRatio > 4 || imgRatio < .25 ?
                    MIN_LOGO_SIZE * 3 : MIN_LOGO_SIZE;
                var availableHeight = parseInt((parent[0].offsetHeight -
                    minLogoSize) / 2);
                var availableWidth = parseInt((parent[0].offsetWidth -
                    minLogoSize) / 2);
                parent.css({
                  paddingTop: Math.min(availableHeight, padding +
                      logoMargins.t) + 'px',
                  paddingRight: Math.min(availableWidth, padding +
                      logoMargins.r) + 'px',
                  paddingBottom: Math.min(availableHeight, padding +
                      logoMargins.b) + 'px',
                  paddingLeft: Math.min(availableWidth, padding +
                      logoMargins.l) + 'px'
                });
                element.addClass('inline-wrapper');
                new ddab.layouts.utils.DynamicImageFit(el, src, attrs.scaletype,
                    attrs.aligntype);
                scope.isLogoPlaced = true;
                scope.$digest();
              }, 0);
            }
            done = true;
          }
        });
      }
    };
  });


  /**
   * Creates a shallow object clone.
   * @param {Object} obj Object to be cloned.
   * @return {!Object} Returns cloned object.
   */
  function clone(obj) {
    var res = {};
    for (var prop in obj) {
      if (obj.hasOwnProperty(prop)) {
        res[prop] = obj[prop];
      }
    }
    return res;
  }


  /**
   * Creates DynamicTextFit and applies alignText on it
   * @param {!angular.Object} el Object of the DOM element to handle.
   */
  function extTextFit(el) {
    var minfontsize = el.attr('minfontsize');
    var multiline = el.attr('multiline');
    var truncate = el.attr('truncate');
    new ddab.layouts.utils.DynamicTextFit(el[0],
        minfontsize && minfontsize.toNumber(),
        multiline && multiline.toBoolean(),
        truncate && truncate.toBoolean());

    alignText(el);
  }


  /**
   * Aligns text in the element.
   * @param {!angular.JQLite} el The jQuery element object to handle.
   */
  function alignText(el) {
    var valign = el.attr('valign');
    var text = wrapText(el, 'span');

    if (valign) {
      el.addClass('inline-wrapper');
      text.css({
        'display': 'inline-block',
        'height': 'auto',
        'vertical-align': valign,
        'width': '100%'
      });
    }
  }


  /**
   * Wraps text into DOM element to apply vertical alignment.
   * @param {!angular.JQLite} el The jQuery element object to handle.
   * @param {string} tagName DOM element name.
   * @return {!Element} Returns text wrapped into newly created DOM element.
   */
  function wrapText(el, tagName) {
    var text = el.text();
    var tagElement = document.createElement(tagName);

    /**
     * @type {Array.<angular.JQLite>}
     */
    var tag = angular.element(tagElement);
    tag.text(text);

    el.css({
      'font-size': window.getComputedStyle(el[0]).getPropertyValue('font-size')
    });
    el.html('');
    if (el.attr('truncate').toBoolean()) {
      tag.css({
        'overflow': 'hidden',
        'text-overflow': 'ellipsis'
      });
      if (!el.attr('multiline').toBoolean()) {
        tag.css({
          'white-space': 'nowrap'
        });
      }
    }

    el.append(tag);
    return tag;
  }


  /**
   * Converts star rating string to an integer, following Google Rating
   * integer-to-star value rules. All the ratings that have remainders larger
   * than .71 are converted to the next integer (eg. 3.5 to 3, and 3.8 to 4).
   * @param {string=} opt_rating Star rating as a string.
   * @return {number} Star rating as an integer number.
   */
  function ratingToInteger(opt_rating) {
    opt_rating = opt_rating || 0;
    var floor = Math.floor(parseFloat(opt_rating));
    var remainder = opt_rating % floor >= StarRating.MAX_DELTA ? 1 : 0;
    return floor + remainder;
  }


  /**
   * Expands shorthand form (e.g. "03F") to full form (e.g. "0033FF").
   * @param {string} hex Color in hexidecimal.
   * @return {string} color in full hexidecimal.
   */
  function getFullHexColor(hex) {
    return hex.replace(RgbChannelsRegExps.SHORT, function(r, g, b) {
      return r + r + g + g + b + b;
    });
  }


  /**
   * Check if the user is using IE.
   * @return {boolean} Whether is IE.
   */
  function isIE() {
    var myNav = navigator.userAgent.toLowerCase();
    return ((myNav.indexOf(ieUserAgentPart.IE_BELOW_V11) != -1) ||
        myNav.indexOf(ieUserAgentPart.IE_V11_AND_ABOVE) != -1);
  }

  return {
    alignText: alignText,
    clone: clone,
    extTextFit: extTextFit,
    isIE: isIE,
    LayoutController: LayoutController,
    wrapText: wrapText
  };
})();
