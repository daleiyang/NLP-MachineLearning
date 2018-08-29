/**
 * @fileoverview Provides common functionality for HTML5 layouts.
 */


/**
 * Utils object with common functionality for the layouts.
 */
var utils = (function() {
  var utils = angular.module('utils', []);
  var rawData = {};
  var dabUtils = {};
  var loadedRes = {};
  var lastInteractedProduct;
  var layoutSpec = {
    meta: {
      layoutName: '',
      version: ''
    },
    attributes: {}
  };

  /**
   * Implements functionality for image preloading.
   * @return {!Object.<function>} Object of public methods for the preloader.
   */
  var preloader = (function() {
    var images = [];
    var listeners = [];
    var cache = {};
    var completed = 0;
    var total = 0;

    /**
     * Creates new image DOM element,
     * binds handlers for possible events,
     * adds passed source path.
     * @param {string} src Image source path.
     * @private
     */
    var load = function(src) {
      var $img = angular.element(new Image());
      $img.bind('load', function() {
        cache[src] = $img;
        progress($img);
      });
      $img.bind('error abort', function() {
        progress($img);
      });
      $img[0].src = src;
    };

    /**
     * Tracks loading progress.
     * @param {angular.Object} $img Angular object of the DOM element to track.
     * @private
     */
    var progress = function($img) {
      if (++completed == total) {
        end();
      }
      $img.unbind('load error abort');
    };

    /**
     * Calls final functions on preload end.
     * @private
     */
    var end = function() {
      fireCompletion();
      clear();
    };

    /**
     * Fires corresponding events on preload completion.
     * @private
     */
    var fireCompletion = function() {
      for (var i = 0; i < listeners.length; i++) {
        listeners[i]();
      }
    };

    /**
     * Clears veriables for the preloader.
     * @private
     */
    var clear = function() {
      images = [];
      listeners = [];
      completed = total = 0;
    };

    return {

      /**
       * Adds image to the preloader queue.
       * @param {string} imgSrc Image source path.
       */
      addImage: function(imgSrc) {
        if (!imgSrc || imgSrc == 'empty') {
          return;
        }
        images.push(imgSrc);
      },

      /**
       * Adds event listener to be fired on load/error.
       * @param {function(...)} callback Function to be called on callback.
       */
      addCompletionListener: function(callback) {
        listeners.push(callback);
      },

      /**
       * Starts preload process.
       */
      start: function() {
        total = images.length;
        if (total == 0) {
          end();
        }
        for (var i = 0; i < total; i++) {
          load(images[i]);
        }
      },

      /**
       * Returns preloaded images.
       * @return {Object.<string, angular.Element>} Object with Angular
       *          img elements.
       */
      getLoadedImages: function() {
        return cache;
      }
    };
  })();


  /**
   * Parses JSON with dynamic data from DAB.
   * @param {Object} json Dynamic data object.
   * @param {string} dataType Parsed data type (eg. Product, Headline, Design)
   * @return {Array.<string, string>} Array of settings with values.
   */
  function parse(json, dataType) {
    var res = [];
    for (var key in json) {
      if (json.hasOwnProperty(key)) {
        var startsWith = key.indexOf(dataType) == 0;

        if (startsWith) {
          var val = json[key];
          var data = key.split('_');
          var ind = data[1];
          var propName = data[2];
          res[ind] = res[ind] || {};
          res[ind][propName] = val;
        }
      }
    }
    return res;
  }


  /**
   * Parse layout data for data binding in layout.
   */
  utils.factory('dynamicData', function() {
    return rawData;
  });


  /**
   * Listen for incoming dynamic data, parse and set up for data binding.
   * @param {Object} data Layout data object.
   */
  function onAdData(data, util) {
    rawData = data;
    dabUtils = util;
    loadedRes = preloader.getLoadedImages();
    angular.bootstrap(document, ['layout']);
    if (typeof(setup) == 'function') {
      setup();
    }
  }

  /**
   * Check if image loaded.
   * @param {String} url.
   * @return {boolean} If the image is loaded returns true.
   */
  function isLoadedRes(url) {
    return loadedRes[url] !== void 0;
  }

  /**
   * Exposes DynamicTextFit as a custom attribute.
   * @return {!angular.Directive} Directive definition object.
   */
  utils.directive('textFit', function() {
    return {
      restrict: 'A',
      link: function($scope, el, attr) {
        setTimeout(function() {
          var dynamicTextFit = new ddab.layouts.utils.DynamicTextFit(el[0],
              Number(attr.minfontsize), attr.multiline, attr.truncate);
        }, 0);
      }
    };
  });

  /**
   * Exposes DynamicImageFit as a custom attribute.
   * @return {!angular.Directive} Directive definition object.
   */
  utils.directive('imageFit', function() {
    return {
      restrict: 'A',
      link: function($scope, el, attr) {
        setTimeout(function() {
          var dynamicImageFit = new ddab.layouts.utils.DynamicImageFit(el[0],
              attr.src, attr.scaletype, attr.aligntype);
        }, 0);
      }
    };
  });

  /**
   * String prototype to know if the string is empty.
   * @return {boolean} If the string is empty returns true.
   */
  String.prototype.isEmpty = function() {
    return this == '';
  };

  /**
   * String prototype to convert string type to boolean.
   * @return {boolean}
   */
  String.prototype.toBoolean = function() {
    return this == 'true';
  };

  /**
   * String prototype to convert string type to number.
   * @return {number}
   */
  String.prototype.toNumber = function() {
    return Number(this);
  };

  /**
   * String prototype to build correct string template.
   * Eg. '{0}px' will be replaced with '15px', if the argument was 15.
   * @return {string} Returns string with the template replaced to real value.
   */
  String.prototype.format = function() {
    var args = arguments;
    return this.replace(/{(\d+)}/g, function(match, number) {
      return typeof args[number] != 'undefined' ? args[number] : match;
    });
  };

  /**
   * String prototype to format string for a CSS color value.
   * @return {?string} Returns color formatted to full HEX value.
   */
  String.prototype.toColor = function() {
    var return_obj = this;
    if (!this) {
      return null;
    }

    if (this.indexOf('#') != -1) {
      var tmp = this.replace(/#/g, '0x');
      return_obj = tmp;
    }

    return '#' + return_obj.split('0x').join('');
  };

  /**
   * String prototype to convert HEX color to RGBA.
   * @param {number=} opt_alpha Accepts alpha,
   *     if no number provided takes 1.
   * @return {?string} Formatted string like "rgba(r,g,b,a)"
   */
  String.prototype.hexToRGBA = function(opt_alpha) {

    opt_alpha = typeof opt_alpha !== 'undefined' ? opt_alpha : 1;

    if (!this) {
      return null;
    }

    var hex = getFullHEXColor(this.toColor());
    var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? 'rgba(' + parseInt(result[1], 16) + ',' +
        parseInt(result[2], 16) + ',' + parseInt(result[3], 16) + ',' +
        opt_alpha + ')' :
        null;
  };

  /**
   * String prototype to change color brightness.
   * @param {number} delta Accepts delta to change brightness.
   *    If delta is between -1 (including) and 0, the color will become darker.
   *    If delta is between 0 and 1 (including), the color will becomde lighter.
   * @return {?string} Formatted string like "rgb(r,g,b)".
   */
  String.prototype.changeBrightness = function(delta) {
    if (!this) {
      return null;
    }

    var hex = getFullHEXColor(this.toColor());
    var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    var rgb = '', part;

    for (var i = 1; i < result.length; i++) {
      part = parseInt(result[i], 16);
      part += part * delta;
      rgb += Math.round(Math.min(Math.max(0, part), 255));

      if (i !== 3) {
        rgb += ',';
      }
    }

    return rgb ? 'rgb(' + rgb + ')' : null;
  };

  /**
   * String prototype to change color lightness using HSL.
   * @param {number} hue Accepts delta to change saturation.
   * @return {?string} Formatted string like "hsl(h,s,l)".
   */
  String.prototype.changeHue = function(hue) {
    hue = hue || 0;
    if (!this) {
      return null;
    }

    var hsl = toHSL_(this.toColor());
    hsl.h = Math.round(Math.min(Math.max(0, hsl.h + parseInt(hue)), 360));

    return 'hsl(' + hsl.h + ', ' +
        hsl.s + '%, ' + hsl.l + '%)';
  };

  /**
   * String prototype to change color lightness using HSL.
   * @param {number} saturation Accepts delta to change saturation.
   * @param {number} lightness Accepts delta to change lightness.
   * @return {string} Formatted string like "hsl(h,s,l)".
   */
  String.prototype.changeSaturationAndLightness =
      function(saturation, lightness) {
    saturation = saturation || 0;
    lightness = lightness || 0;
    if (this == '') {
      return null;
    }

    var hsl = toHSL_(this.toColor());
    hsl.s = Math.round(Math.min(Math.max(0, hsl.s +
        parseInt(saturation)), 100));
    hsl.l = Math.round(Math.min(Math.max(0, hsl.l +
        parseInt(lightness)), 100));

    return 'hsl(' + hsl.h + ', ' +
        hsl.s + '%, ' + hsl.l + '%)';
  };

  /**
   * Converts an HEX color value to HSL. Conversion formula
   * adapted from http://en.wikipedia.org/wiki/HSL_color_space.
   * @return {Object} The HSL representation.
   */
  function toHSL_(hex) {
    if (!this) {
      return null;
    }

    hex = getFullHEXColor(hex);
    var rgb = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);

    var r = parseInt(rgb[1], 16) / 255,
        g = parseInt(rgb[2], 16) / 255,
        b = parseInt(rgb[3], 16) / 255;

    var max = Math.max(r, g, b), min = Math.min(r, g, b);
    var h, s, l = (max + min) / 2;

    if (max === min) {
      h = s = 0; // achromatic
    } else {
      var d = max - min;
      s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
      switch (max) {
        case r: h = (g - b) / d + (g < b ? 6 : 0); break;
        case g: h = (b - r) / d + 2; break;
        case b: h = (r - g) / d + 4; break;
      }
      h /= 6;
    }

    return {
      h: Math.floor(h * 360),
      s: Math.floor(s * 100),
      l: Math.floor(l * 100)
    };
  }

  /**
   * Expands shorthand form (e.g. "03F") to full form (e.g. "0033FF").
   * @param {string} hex Color in HEX.
   * @return {string} color in full HEX.
   */
  function getFullHEXColor(hex) {
    var shorthandRegex = /^#?([a-f\d])([a-f\d])([a-f\d])$/i;
    return hex.replace(shorthandRegex, function(r, g, b) {
      return r + r + g + g + b + b;
    });
  }


  /**
   * Gets value from dynamicData by its property.
   * @param {string} property Property to get the value by.
   * @return {string|number|boolean} Corresponding value.
   */
  function getValue(property) {
    if (rawData.google_template_data.adData[0][property]) {
      return rawData.google_template_data.adData[0][property];
    }

    return false;
  }


  /**
   * Defines attributes in layout spec.
   * @param {string} itemType Item type (Product|Headline|Design).
   * @param {string} attribute Item attribute name.
   * @param {boolean} required Defines whether the attribute is required.
   */
  function defineAttribute(itemType, attribute, required) {
    if (!layoutSpec.attributes[itemType]) {
      layoutSpec.attributes[itemType] = {};
    }
    layoutSpec.attributes[itemType][attribute] = {
      itemType: itemType,
      attribute: attribute,
      required: required
    };
  }

  /**
   * Defines meta information for the layout spec.
   * @param {string} key Meta information title.
   * @param {string} value Meta information data.
   */
  function defineMeta(key, value) {
    layoutSpec.meta[key] = value;
  }


  /**
   * Defines maximum and minimum number of available products in the layout.
   * @param {string} itemType Defines the type of item.
   * @param {number} min Minimum products number.
   * @param {number} max Maximun products number.
   */
  function defineOccurrences(itemType, min, max) {
    if (!layoutSpec.meta.occurrences) {
      layoutSpec.meta.occurrences = {};
    }
    layoutSpec.meta.occurrences[itemType] = {
      minOccurrences: min,
      maxOccurrences: max
    };
  }


  /**
   * Image preloader.
   * @param {string} src Image source path.
   * @param {function(...)} success Success callback function.
   * @param {function(...)} failure Failure callback function.
   */
  function preload(src, success, failure) {
    var doNothing = function() {};
    success = success || doNothing;
    failure = failure || doNothing;
    if (src !== void 0 && loadedRes[src] !== void 0) {
      success(loadedRes[src][0]);
    } else {
      failure();
    }
  }


  /**
   * Exposes additional margins for the logo from custom attributes.
   * @param {!angular.Element} $el Angular element to get the logo margins.
   * @return {{t: Number, r: Number, b: Number, l: Number}} Object with margins.
   */
  function logoMargin($el) {
    var top = $el.attr('logo-margin-top') || 0,
        right = $el.attr('logo-margin-right') || 0,
        bottom = $el.attr('logo-margin-bottom') || 0,
        left = $el.attr('logo-margin-left') || 0;
    return {
      t: parseInt(top),
      r: parseInt(right),
      b: parseInt(bottom),
      l: parseInt(left)
    };
  }

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
   * Gets layout specification.
   * @return {{meta: {layoutName: string, version: string}, attributes: {}}}
   */
  function getLayoutSpec() {
    return layoutSpec;
  }


  /**
   * Handles the click on the ad.
   * @param {!Event} event Event object.
   */
  function clickHandler(event) {
    var adContainer = document.getElementById('ad-container');
    var fieldReference = adContainer.getAttribute('field-reference');

    if (fieldReference) {
      dabUtils.exit(fieldReference);
    } else {
      dabUtils.exit();
    }
  }

  angular.module('layout', ['utils']);

  return {
    clickHandler: clickHandler,
    defineAttribute: defineAttribute,
    defineMeta: defineMeta,
    defineOccurrences: defineOccurrences,
    getFullHEXColor: getFullHEXColor,
    getLayoutSpec: getLayoutSpec,
    getValue: getValue,
    isLoadedRes: isLoadedRes,
    logoMargin: logoMargin,
    onAdData: onAdData,
    parse: parse,
    preload: preload,
    preloader: preloader
  };
})();

// Expose top level variables where required for tooling.
var getLayoutSpec = utils.getLayoutSpec;
var onAdData = utils.onAdData;
