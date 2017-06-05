<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/streetview/publish/v1/rpcmessages.proto

namespace Google\Streetview\Publish\V1;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * <pre>
 * Request to create a photo.
 * </pre>
 *
 * Protobuf type <code>google.streetview.publish.v1.CreatePhotoRequest</code>
 */
class CreatePhotoRequest extends \Google\Protobuf\Internal\Message
{
    /**
     * <pre>
     * Required. Photo to create.
     * </pre>
     *
     * <code>.google.streetview.publish.v1.Photo photo = 1;</code>
     */
    private $photo = null;

    public function __construct() {
        \GPBMetadata\Google\Streetview\Publish\V1\Rpcmessages::initOnce();
        parent::__construct();
    }

    /**
     * <pre>
     * Required. Photo to create.
     * </pre>
     *
     * <code>.google.streetview.publish.v1.Photo photo = 1;</code>
     */
    public function getPhoto()
    {
        return $this->photo;
    }

    /**
     * <pre>
     * Required. Photo to create.
     * </pre>
     *
     * <code>.google.streetview.publish.v1.Photo photo = 1;</code>
     */
    public function setPhoto(&$var)
    {
        GPBUtil::checkMessage($var, \Google\Streetview\Publish\V1\Photo::class);
        $this->photo = $var;
    }

}

